"""
Author: Muhammad Zaki FUadi
Date: 12/05/2023
This is the pipeline.py module.
Usage:
- Create TFX Pipeline
"""

import os
from typing import Text

from absl import logging
from tfx.orchestration import metadata, pipeline
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner

PIPELINE_NAME = 'chrun-pipeline'

DATA_ROOT = 'data'
TRANSFORM_MODULE_FILE = 'modules/transform.py'
TRAINER_MODULE_FILE = 'modules/trainer.py'

OUTPUT_BASE = 'outputs'
serving_model_dir = os.path.join(OUTPUT_BASE, 'serving_model')
pipeline_root = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
metadata_path = os.path.join(pipeline_root, 'metadata.sqlite')


def init_local_pipeline(
    components, pipeline_root: Text
) -> pipeline.Pipeline:
    """
    Initialize a local TFX pipeline.

    Args:
        components: A dictionary of TFX components to be included in the pipeline.
        pipeline_root: Root directory for pipeline output artifacts.

    Returns:
        A TFX pipeline.
    """
    logging.info(f'Pipeline root set to: {pipeline_root}')
    beam_args = [
        '--direct_running_mode=multi_processing'
        # 0 auto-detect based on the number of CPUs available
        # duraing execution time
        '----direct_num_workers=0'
    ]

    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            metadata_path
        ),
        eam_pipeline_args=beam_args
    )


if __name__ == '__main__':
    logging.set_verbosity(logging.INFO)

    from modules.components import init_components
    components = init_components(
        DATA_ROOT,
        training_module=TRAINER_MODULE_FILE,
        transform_module=TRANSFORM_MODULE_FILE,
        training_steps=1000,
        eval_steps=800,
        serving_model_dir=serving_model_dir,
    )

    pipeline = init_local_pipeline(components, pipeline_root)
    BeamDagRunner().run(pipeline=pipeline)
