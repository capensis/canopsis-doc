Event Feeder
============

L'event feeder est un outil permettant de simuler des envois (massifs) d'events
canopsis.

Le feeder actuel remplace une première version qui ne gérait pas tous les
types d'events et qui faisait des trop grosses approximations sur les
probabilités. Le nouveau feeder est capable d'envoyer tous les types d'event
[1]_ et tente de simuler les interactions de manière réaliste.

Il est non seulement possible d'envoyer des events déterministes, mais aussi de
simuler le workflow des actions utilisateur (ack, ackremove, cancel, uncancel,
changestate...) à l'aide de probabilités et de délais.

Le feeder intègre aussi un outil de scenario permettant de lancer des scenario
en parallèle du fonctionnement classique. L'outil de scenario reste utilisable
indépendamment.

.. [1] Pour l'instant, il ne permet pas l'envoi d'events calendar et
   declareticket. Ils seront rajoutés lorsqu'il aura été vérifié que Canopsis
   peut les enregistrer.

Composition
-----------

Le feeder est composé de plusieurs parties :

   - scripts/canopsis-feed : Script principal du 'feeder', ordonance les events
   - scripts/canopsis-scenario : Envoie des events en mode scenario
   - scripts/canopsis-splitconf : Découpe la configuration au format attendu
     par les scripts
   - etc/feeder_monolithic.json : Fichier de configuration principal. Ce n'est
     pas lui qui est lu par le feeder. Il doit être découpé en plusieurs petits
     fichiers à l'aide de scripts/canopsis-splitconf.py.
   - etc/scenario/<scenario>.py : Définitions des scenario au format attendu

Dépendances
-----------

Il n'y a pas besoin d'un environnement canopsis. La seule dépendance est le
package kombu. Cette dépendance est gérée par setuptools.

Par contre, cette dépendance implique d'avoir une connection internet lors de
l'installation. Il n'y a pas de méthode préconfigurée pour une installation
hors ligne.

Principe de fonctionnement
--------------------------

Le feeder se base sur les valeurs numériques et les probabilités renseignées
pour simuler un site de production.

Il utilise différents 'processeurs' pour l'ordonnancement :

   - DeterministProcessor : Des événements prévisibles (user, log, calendar),
     et dont l'état n'a pas besoin d'être enregistré pour d'autres envois.
   - AlarmProcessor : Événements check/eue et leur workflow. Chaque action
     utilisateur possible est testée, puis réalisée. Les changements d'état
     se font en fonction d'une probabilité et d'un délais minimal avec la
     dernière action.
   - ScenarioProcessor : Les événements définis dans le scenario sont envoyés
     un par un. Le scenario peut être lancé en boucle continue.

Chaque seconde est ordonnancée une vague d'événements de chaque type.

Configuration
-------------

Remarques générales :

   - Les probabilités doivent être comprises entre 0 et 1
   - Les délais sont en seconde
   - Certaines valeurs ne peuvent pas être inférieures à 0 ou 1
   - Seules les probabilités sont de type float. Les autres valeurs numériques
     seront castées en int s'il le faut.

Connection amqp :
~~~~~~~~~~~~~~~~~

   .. code:: json

      "amqp": {
          "user": "cpsrabbit",
          "passwd": "canopsis",
          "host": "localhost",
          "port": 5672,
          "vhost": "canopsis"
      }

Events check :
~~~~~~~~~~~~~~

   - normal_check_time : Tous les events check seront envoyés à cette période.
     Dans l'exemple, on enverra (20 * 100 + 20) / 10 = 200 checks par seconde.
   - max_KO_rate : Taux maximal d'état KO. Les checks KO sont choisis à
     l'initialisation, avant d'envoyer les premiers. Ce taux maximal est
     également le taux initial.
   - perf_data : Des perfdatas seront attachées à certains events check.
     components * resources_per_component * publish_rate perfdatas seront
     attachées. Il y aura entre 1 et max_metric metriques pour chaque perfdata.

   .. code:: json

      "check": {
          "components": 20,
          "resources_per_component": 100,
          "normal_check_time": 10,
          "max_KO_rate": 0.5,
          "changestate_rate": [
              ["KO_to_OK", 0.2],
              ["OK_to_KO", 0.2]
          ],
          "changestate_delay": 4
          "perf_data": {
             "publish_rate": 0.5,
             "max_metric": 5
          },
      }

.. warning:: (20 * 100 + 20) / 10 = 200 checks par seconde. Le nombre total
   d'alarme sera arrondi à 20 * 10 = 2000, et non pas 2020. Les 20 dernières
   seront ignorées.

Events EUE :
~~~~~~~~~~~~

Les events EUE sont traités de manière similaire aux events check.

   .. code:: json

      "eue": {
           "features": 8,
           "scenarii_per_feature": 10,
           "steps_per_scenario": 12,
           "normal_check_time": 30,
           "max_KO_rate": 0.02,
           "changestate_rate" : [
               ["KO_to_OK", 0.01],
               ["OK_to_KO", 0.01]
           ],
           "changestate_delay": 10,
           "perf_data": {
              "publish_rate": 0.5,
              "max_metric": 5
           },
           "cntxt_localization": [
               "loc1",
               "loc2",
               "loc3"
           ],
           "cntxt_os": [
               "windows",
               "linux",
               "mac"
           ],
           "cntxt_browser": [
               "firefox",
               "chrome",
               "ie"
           ],
           "cntxt_env": [
               "PROD",
               "PREPROD",
               "TEST"
           ]
    }

Alarmes :
~~~~~~~~~

On appelera alarme un event qui peut potentiellement être KO, c'est à dire s'il
est de type check ou EUE.

Sur l'UI, plusieurs actions sont possibles en fonction de l'état de ce KO
(default, ack, cancel). Ces états sont appelés nodes, nodes du workflow des
alarmes.

À chaque node il y a une liste d'actions possibles, dont on peut configurer
probabilité et délai minimum.

   .. code:: json

      "alarm_workflow": {
          "default": {
              "ack": {
                  "switch_probability": 0.01,
                  "switch_delay": 1
              }
          },
          "ack": {
              "ackremove": {
                  "switch_probability": 0.01,
                  "switch_delay": 1
              },
              "declare-ticket": {
                  "switch_probability": 0.0,
                  "switch_delay": 10
              },
              "assocticket": {
                  "switch_probability": 0.01,
                  "switch_delay": 10
              }
              "cancel": {
                  "switch_probability": 0.01,
                  "switch_delay": 1
              }
          },
          "cancel": {
              "uncancel": {
                  "switch_probability": 0.01,
                  "switch_delay": 1
              },
              "declare-ticket": {
                  "switch_probability": 0.0,
                  "switch_delay": 10
              },
              "assocticket": {
                  "switch_probability": 0.01,
                  "switch_delay": 10
              }
          }
      }

Workflow anytime events sont les événements sur les alarmes applicables à
n'importe quel moment du workflow.

   .. code:: json

      "workflow_anytime_event": {
           "changestate": {
               "probability": 0.2,
               "delay": 1
           }
      }

Et alarm anytime event concerne les actions applicables peut importe que l'état
de l'alarme soit KO ou OK.

   .. code:: json

      "alarm_anytime_event": {
          "downtime": {
              "probability": 0.2,
              "delay": 2
          }
      }

.. warning:: Il faut donc faire attention s'il y a un très grand nombre
   d'entités au total (disons 20 000) et un petit nombre envoyé à chaque
   période (500). Le taux de déclenchement du downtime sera calculé par
   rapport aux 20 000 et doit donc être faible.

Événements déterministes :
~~~~~~~~~~~~~~~~~~~~~~~~~~

Les événements déterministes sont indépendants de tout le reste. Ils peuvent
juste être envoyés sans avoir besoin de les garder en mémoire pour le reste de
la simulation. Pas encore implémentés.

   .. code:: json

      "determinist_events": {
          "calendar": {
              "output": 5
          },
          "user": {
              "output": 3
          },
          "log": {
              "output": 3
          }
      }

Custom fields :
~~~~~~~~~~~~~~~

Les custom fields peuvent être renseignés pour écrire des champs personnalisés
dans les événements. Le feeder se charge de remplir tous les champs
obligatoires pour chaque type d'event avec des valeurs par défaut.

La clef global concerne tous les events. Ces valeurs seront surchargées si
elles sont définies par type d'événement.

   .. code:: json

      "custom_fields": {
          "global": {
              "connector": "feeder",
              "connector_name": "feeder1",
              "domain": "feederdomain",
              "perimeter": "feederperimeter"
          },
          "check": {

          },
          "eue": {

          },
          "ack": {

          },
          "ackremove": {

          },
          "cancel": {

          },
          "uncancel": {

          },
          "declare-ticket": {

          },
          "assocticket": {

          },
          "changestate": {

          },
          "downtime": {

          },
          "log": {

          },
          "user": {

          },
          "calendar": {

          }
      }

Utilisation
-----------

Mise en place
~~~~~~~~~~~~~

Après avoir récupéré les sources,

.. code:: bash

   git clone http://github.com/capensis/canopsis-cat

le feeder peut être installé sur le système :

.. code:: bash

   cd canopsis-cat/sources/install.d
   sudo make -f feeder.make install

L'installation va copier des fichiers dans /usr/share/canopsis/scenario. Si
ce chemin ne convient pas (installation dans l'environnement Canopsis par
exemple) on peut faire un make en changeant la variable PREFIX :

.. code:: bash

   sudo make -f feeder.make PREFIX=/opt/canopsis install 

Ensuite, on peut éditer la configuration dans etc/feeder_monolithic.json. Les
scripts ne prendront pas en compte ce fichier, mais des petits fichiers générés
dans etc avec le script canopsis-splitconf :

.. code:: bash

   cd ../python/feeder
   vim etc/feeder_monolithic.json
   canopsis-splitconf.py -j etc/feeder_monolithic.json

Lancement :

(Dans les exemples suivants, si un répertoire etc est présent dans le dossier
actuel, ce qui est le cas si les commandes sont lancées depuis
sources/python/feeder, c'est celui-ci qui sera utilisé si l'option -c n'est pas
fournie.)

feed.py
~~~~~~~

.. code:: bash

   canopsis-feed -d <seconds> -c etc [options]

scenario.py
~~~~~~~~~~~

.. code:: bash

   canopsis-scenario run etc/scenario/<scenario>.py -c etc [options]

canopsis-scenario sera amené à utiliser les fichiers json dans etc qui ne sont
pas contenus dans etc/feeder.

.. info:: si le nom du scenario est spécifié directement, la recherche se fera
   dans le dossier /usr/share/canopsis/scenario, répertoire où sont installés
   tous les scenario par défaut.

   Ces deux commandes sont donc équivalentes :

   canopsis-scenario run /usr/share/canopsis/scenario/<scenario>.py
   canopsis-scenario run <scenario>

