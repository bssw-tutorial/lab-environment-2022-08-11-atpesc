My Study Executive Summary
--------------------------
This repository encapsulates the computational laboratory environment
constructed and used for our 2022 My Study scientific research.  Not only does
it contain all tools needed to setup and use the environment, but it also
contains the metadata and context needed to understand how data was acquired and
how to use it for analysis and drawing conclusions.

Study Goals
-----------
Our motivation for this study is ...

We believe that ...

We intend to use our software to ...

To accomplish our goals we require that ...

We understand that our software is limited and therefore that our study is
limited in the sense that ...

Some optional goals are ...

Ideally, we would like to publish our results in the Journal ZYX with a
submission target date of ...

Organization
------------
ABC will be the PI and will ...

XYZ is responsible for ...

The gatekeepers are ...

All action items are being managed through the Kanban board associated with this
repo.

Lab Env Workflow
----------------
This repo is structured *as if* data acquired during the study is to be
committed to the repo.  However, due to the large amount of data to be acquired
and the large size of each file, we *do not* commit the data to the repo.

Gatekeepers will maintain a read-only version of this repo in a shared location
and such that all study participants have access to the data.  This version is
known as the "data clone" and is protected, backed-up, and should exist in
perpetuity -- it is the official record of the study and should help guarantee
rigor and reproducibility.  Once data has been acquired and it is determined
that the data will support this study, the data should be given to the
gatekeepers for inclusion in the data clone.  All analysis that supports the
study should eventually use only data in the data clone.

One goal of this repo design is to place the metadata and context as close as
possible to its associated data.  The hope is that all participants will be able
to visit the data clone in the future to easily understand what was done and
why.

The gatekeepers also construct software environments for building and executing
our study's binaries.  These are located in the data clone and all participants
are encouraged to use these resources.

Participants should not use any content in the data clone other than the data
and the SW environment tools.  Instead, each participant should construct their
own "work clone" and use this for acquiring data, developing analysis
tools/scripts, and documenting their work.

Each participant must create and use where appropriate the environment variables
1. MYSTUDY_DATA_CLONE - the full path to the data clone maintained by the
gatekeepers
2. MYSTUDY_WORK_CLONE - the full path to the participant's work clone.

So that all figures included in the article have a similar look and feel and to
ease tweaking figure geometries, please use the values in the file
`esthetics.json` to construct your figures.

Lab Notes
---------
* __Phase 1__ - Characterize all four systems of interest by running the standard
simulation with the four gold standard configurations as determined by our
community.  We expect to see important differences in the data that reflect the
different physics channels enabled by the different configs.
  * ABC was troubled by the similarity of the summary statistics across all
    systems.  This lead to phase 2.
* __Phase 2__ - Repeat phase 1 but with the software altered to save data at a
 finer level.
  * ABC's hunch was correct.  The finer data revealed that the systems are
    strongly different despite having similar summary statistics.
* __Next phase?!__
