dataset_type = "TrainDatasetForStudents"


train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    
    dict(type='RandomResize', scale=(512, 512), ratio_range=(0.5, 2.0), keep_ratio=True),
    dict(type='RandomCrop', crop_size=(512, 512), cat_max_ratio=0.75),
    
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    
    dict(type='PackSegInputs'),
]

train_dataset = dict(
    type=dataset_type,
    data_root="mmsegmentation/data/train_dataset_for_students",
    data_prefix=dict(
        img_path='img/train',
        seg_map_path='labels/train',
    ), 
    pipeline=train_pipeline,
    img_suffix=".jpg",
    seg_map_suffix=".png",
)

train_dataloader = dict(
    batch_size=16,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=train_dataset
)

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataset = dataset=dict(
    type=dataset_type,
    data_root='mmsegmentation/data/train_dataset_for_students',
    data_prefix=dict(
        img_path='img/test',
        seg_map_path='labels/test'),
    pipeline=test_pipeline,
    img_suffix=".jpg",
    seg_map_suffix=".png"
)
test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=test_dataset
)

val_pipeline = test_pipeline
val_dataset = dataset=dict(
    type=dataset_type,
    data_root='mmsegmentation/data/train_dataset_for_students',
    data_prefix=dict(
        img_path='img/val',
        seg_map_path='labels/val'),
    pipeline=test_pipeline,
    img_suffix=".jpg",
    seg_map_suffix=".png"
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=test_dataset
)

val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
test_evaluator = val_evaluator 