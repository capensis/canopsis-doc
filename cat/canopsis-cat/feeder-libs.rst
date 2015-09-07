Feeder API
==========

This document describe globally every part of the feeder feeder. After reading
it, you should be able to use feeder as a libraries to send events to Canopsis.

Keep in mind that it is a global description. For more detail, docstrings and
commentaries should answer your questions.

Structure
---------

The feeder projet is composed of :

   - scripts
   - json configuration
   - python 'configuration' (scenario)
   - modules

Scripts
^^^^^^^
split_conf.py splits etc/feeder_monolithic.json into little json files.

feed.py instanciates a Scheduler (module scheduler) and pilotes it. The
Scheduler instanciates an AlarmProcessor, a DeterministProcessor, a
ScenarioProcessor (if a scenario name has been supplied) and pilote them.

scenario.py instanciates a ScenarioProcessor and pilotes it. Though feed.py
allows to process scenario, this is more convenient to have a dedicated script
for this task, because in a lot of cases you just need to send a scenario.

JSON configuration
^^^^^^^^^^^^^^^^^^
JSON configuration can be found in etc/feeder_monolithic.json. Once split by
split_conf.py, six more files a created : etc/amqp.json,
etc/custom_fields.json, etc/feeder/determinists.json, etc/feeder/workflow.json,
etc/feeder/check.json, etc/feeder/eue.json.

Files in etc/feeder are useful only in the feeder context. Other json files can
be used both by feed.py and scenario.py.

Python configuration (scenario)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Those files describe scenario. They will be imported by the ScenarioProcessor
and processed by it. What those 'configuration' files achieve is only to
describe the steps to the processor.

Scenario can be found in etc/scenario. You can also find those files in
/usr/share/canopsis/scenario if you have installed the feeder like bellow :

.. code:: bash

   cd source/install.d
   make feeder.make install

An example with a lot of commentaries on how a scenario can (and must) be built
can be found in etc/scenario/example.py.

Modules
^^^^^^^
All feeder modules are in canopsis/feeder/canopsis. Once you have installed the
feeder (which is _not_ installed by the CAT installer), you can import those
modules :

.. code:: python
   
   import canopsis.feeder.module

Most of them are tested in a unitary way.

Functionnal description
-----------------------

Each module will be explained briefly.

amqp.py
^^^^^^^
Handles amqp connection with a singleton pattern. A unique method allows you to
send events without ref_rk.

If you want to send events forged by your own, you can use it. Else, you can
ignore it.

ConfigurationConverter.py
^^^^^^^^^^^^^^^^^^^^^^^^^
Converts JSON configuration pieces to python dictionnaries. Some fields are
added, other dropped.

Instead of reading this module to understand parameters format, you can also
check unit tests.

DeterministProcessor.py, AlarmProcessor.py, ScenarioProcessor.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
They are very similar. Each one of them has a class which calculates and sends
events.

Their constructor build an initial situation from given parameters. An event
flow is sent each time the process method is called. The flow depends on the
processor. For instance ScenarioProcessor will send only the next step.

Only the process method should be triggered from outside.

InitEue.py, InitCheck.py
^^^^^^^^^^^^^^^^^^^^^^^^
Check and eue events share the same workflow, but not the same structure.
That's why they are initialized differently and processed in a shared module.

scheduler.py
^^^^^^^^^^^^
This module allows to pilote the three processors with a single method :
process.

EventBuilder.py
^^^^^^^^^^^^^^^
An interface which creates events easily (singleton pattern). Using this
tool ensures your events to have all mandatory fields (if a field is not
provided, a generic value is inserted). It can be configured to have other
default values than generic ones.

utils.py
^^^^^^^^
Provide utils that are strongly tied with inner mechanics of other modules. You
should ignore it.

The only function that can be useful is ref_rk.

ScenarioUtils.py
^^^^^^^^^^^^^^^^
Defines scenario macros. It might happen you need to patch it (and
ScenarioProcessor) to add a new macro behaviour. Read module docstring for more
infos.
