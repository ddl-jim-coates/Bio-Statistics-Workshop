# workflow.py
import os
from flytekit import workflow, task
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask
from flytekitplugins.domino.task import DatasetSnapshot  


@workflow
def clinical_trial_adverse_event_prediction_workflow():
    transformed_filename = 'transformed_trial_data.csv'  # Clinical trial data filename
    dataset_id = os.environ['dataset_id']

    ada_training_task = DominoJobTask(
        name='Train AdaBoost classifier',
        domino_job_config=DominoJobConfig(Command="python exercises/d_TrainingAndEvaluation/trainer_ada.py", HardwareTierId="large-k8s"),
        inputs={'transformed_filename': str},
        outputs={'results': str},
        use_latest=True,
        cache=True,
        DatasetSnapshots=[DatasetSnapshot(Id=dataset_id, Version=1)]
    )

    gnb_training_task = DominoJobTask(
        name='Train GaussianNB classifier',
        domino_job_config=DominoJobConfig(Command="python exercises/d_TrainingAndEvaluation/trainer_gnb.py", HardwareTierId="large-k8s"),
        inputs={'transformed_filename': str},
        outputs={'results': str},
        use_latest=True,
        cache=True,
        DatasetSnapshots=[DatasetSnapshot(Id=dataset_id, Version=1)]    )
    
    xgb_training_task = DominoJobTask(
        name='Train XGBoost classifier',
        domino_job_config=DominoJobConfig(Command="python exercises/d_TrainingAndEvaluation/trainer_xgb.py", HardwareTierId="large-k8s"),
        inputs={'transformed_filename': str},
        outputs={'results': str},
        use_latest=True,
        cache=True,
        DatasetSnapshots=[DatasetSnapshot(Id=dataset_id, Version=1)]
    )

    ada_results = ada_training_task(transformed_filename=transformed_filename)
    gnb_results = gnb_training_task(transformed_filename=transformed_filename)
    xgb_results = xgb_training_task(transformed_filename=transformed_filename)
    
    compare_task = DominoJobTask(
        name='Compare training results',
        domino_job_config=DominoJobConfig(Command="python exercises/d_TrainingAndEvaluation/compare.py"),
        inputs={'ada_results': str, 'gnb_results': str, 'xgb_results': str},
        outputs={'consolidated': str}, 
        use_latest=True
    )
    
    comparison = compare_task(ada_results=ada_results, gnb_results=gnb_results, xgb_results=xgb_results)

    return comparison
