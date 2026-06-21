data_preprocessor = dict(
    bgr_to_rgb=True,
    mean=[
        123.675,
        116.28,
        103.53,
    ],
    pad_val=0,
    seg_pad_val=0,
    size=(
        512,
        512,
    ),
    std=[
        58.395,
        57.12,
        57.375,
    ],
    type='SegDataPreProcessor')
dataset_type = 'TrainDatasetForStudents'
default_hooks = dict(
    checkpoint=dict(by_epoch=True, interval=5, type='CheckpointHook'),
    logger=dict(interval=20, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(draw=True, interval=1, type='SegVisualizationHook'))
default_scope = 'mmseg'
env_cfg = dict(
    cudnn_benchmark=True,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
input_size = (
    512,
    512,
)
load_from = 'mmsegmentation/practicum_work/artifacts/deeplabv3_experiment1/epoch_15.pth'
log_level = 'INFO'
log_processor = dict(by_epoch=False)
model = dict(
    auxiliary_head=dict(
        align_corners=False,
        channels=256,
        concat_input=False,
        dropout_ratio=0.1,
        in_channels=1024,
        in_index=2,
        loss_decode=[
            dict(
                class_weight=[
                    0.065,
                    1.0,
                    1.3,
                ],
                loss_weight=0.4,
                type='CrossEntropyLoss',
                use_sigmoid=False),
            dict(loss_weight=0.4, type='DiceLoss', use_sigmoid=False),
        ],
        norm_cfg=dict(requires_grad=True, type='SyncBN'),
        num_classes=3,
        num_convs=1,
        type='FCNHead'),
    backbone=dict(
        contract_dilation=True,
        depth=50,
        dilations=(
            1,
            1,
            2,
            4,
        ),
        norm_cfg=dict(requires_grad=True, type='SyncBN'),
        norm_eval=False,
        num_stages=4,
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        strides=(
            1,
            2,
            1,
            1,
        ),
        style='pytorch',
        type='ResNetV1c'),
    data_preprocessor=dict(
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_val=0,
        seg_pad_val=0,
        size=(
            512,
            512,
        ),
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='SegDataPreProcessor'),
    decode_head=dict(
        align_corners=False,
        channels=512,
        dilations=(
            1,
            12,
            24,
            36,
        ),
        dropout_ratio=0.1,
        in_channels=2048,
        in_index=3,
        loss_decode=[
            dict(
                class_weight=[
                    0.065,
                    1.0,
                    1.3,
                ],
                loss_weight=1.0,
                type='CrossEntropyLoss',
                use_sigmoid=False),
            dict(loss_weight=1.0, type='DiceLoss', use_sigmoid=False),
        ],
        norm_cfg=dict(requires_grad=True, type='SyncBN'),
        num_classes=3,
        type='ASPPHead'),
    pretrained='open-mmlab://resnet50_v1c',
    test_cfg=dict(mode='whole'),
    train_cfg=dict(),
    type='EncoderDecoder')
norm_cfg = dict(requires_grad=True, type='SyncBN')
optim_wrapper = dict(
    clip_grad=dict(max_norm=35, norm_type=2),
    optimizer=dict(lr=0.001, momentum=0.9, type='SGD', weight_decay=0.0005),
    type='OptimWrapper')
optimizer = dict(lr=0.001, momentum=0.9, type='SGD', weight_decay=0.0005)
param_scheduler = [
    dict(begin=0, by_epoch=True, end=1, start_factor=0.1, type='LinearLR'),
    dict(
        begin=1,
        by_epoch=True,
        end=100,
        eta_min=0.0001,
        power=0.9,
        type='PolyLR'),
]
resume = False
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=4,
    dataset=dict(
        data_prefix=dict(img_path='img/test', seg_map_path='labels/test'),
        data_root='mmsegmentation/data/train_dataset_for_students',
        img_suffix='.jpg',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(keep_ratio=False, scale=(
                512,
                512,
            ), type='Resize'),
            dict(type='LoadAnnotations'),
            dict(type='PackSegInputs'),
        ],
        seg_map_suffix='.png',
        type='TrainDatasetForStudents'),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_dataset = dict(
    data_prefix=dict(img_path='img/test', seg_map_path='labels/test'),
    data_root='mmsegmentation/data/train_dataset_for_students',
    img_suffix='.jpg',
    pipeline=[
        dict(type='LoadImageFromFile'),
        dict(keep_ratio=False, scale=(
            512,
            512,
        ), type='Resize'),
        dict(type='LoadAnnotations'),
        dict(type='PackSegInputs'),
    ],
    seg_map_suffix='.png',
    type='TrainDatasetForStudents')
test_evaluator = dict(
    iou_metrics=[
        'mIoU',
        'mDice',
    ],
    output_dir=
    'mmsegmentation/practicum_work/artifacts/results/deeplabv3_experiment1/images',
    type='IoUMetric')
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(keep_ratio=False, scale=(
        512,
        512,
    ), type='Resize'),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs'),
]
train_cfg = dict(max_epochs=100, type='EpochBasedTrainLoop')
train_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_prefix=dict(
            img_path='img/train', seg_map_path='labels/train_fixed'),
        data_root='mmsegmentation/data/train_dataset_for_students',
        img_suffix='.jpg',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='LoadAnnotations'),
            dict(
                keep_ratio=True,
                ratio_range=(
                    0.5,
                    2.0,
                ),
                scale=(
                    512,
                    512,
                ),
                type='RandomResize'),
            dict(
                cat_max_ratio=0.75, crop_size=(
                    512,
                    512,
                ), type='RandomCrop'),
            dict(prob=0.5, type='RandomFlip'),
            dict(type='PhotoMetricDistortion'),
            dict(type='PackSegInputs'),
        ],
        seg_map_suffix='.png',
        type='TrainDatasetForStudents'),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_dataset = dict(
    data_prefix=dict(img_path='img/train', seg_map_path='labels/train_fixed'),
    data_root='mmsegmentation/data/train_dataset_for_students',
    img_suffix='.jpg',
    pipeline=[
        dict(type='LoadImageFromFile'),
        dict(type='LoadAnnotations'),
        dict(
            keep_ratio=True,
            ratio_range=(
                0.5,
                2.0,
            ),
            scale=(
                512,
                512,
            ),
            type='RandomResize'),
        dict(cat_max_ratio=0.75, crop_size=(
            512,
            512,
        ), type='RandomCrop'),
        dict(prob=0.5, type='RandomFlip'),
        dict(type='PhotoMetricDistortion'),
        dict(type='PackSegInputs'),
    ],
    seg_map_suffix='.png',
    type='TrainDatasetForStudents')
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(
        keep_ratio=True,
        ratio_range=(
            0.5,
            2.0,
        ),
        scale=(
            512,
            512,
        ),
        type='RandomResize'),
    dict(cat_max_ratio=0.75, crop_size=(
        512,
        512,
    ), type='RandomCrop'),
    dict(prob=0.5, type='RandomFlip'),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs'),
]
tta_model = dict(type='SegTTAModel')
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_prefix=dict(img_path='img/val', seg_map_path='labels/val'),
        data_root='mmsegmentation/data/train_dataset_for_students',
        img_suffix='.jpg',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(keep_ratio=False, scale=(
                512,
                512,
            ), type='Resize'),
            dict(type='LoadAnnotations'),
            dict(type='PackSegInputs'),
        ],
        seg_map_suffix='.png',
        type='TrainDatasetForStudents'),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_dataset = dict(
    data_prefix=dict(img_path='img/val', seg_map_path='labels/val'),
    data_root='mmsegmentation/data/train_dataset_for_students',
    img_suffix='.jpg',
    pipeline=[
        dict(type='LoadImageFromFile'),
        dict(keep_ratio=False, scale=(
            512,
            512,
        ), type='Resize'),
        dict(type='LoadAnnotations'),
        dict(type='PackSegInputs'),
    ],
    seg_map_suffix='.png',
    type='TrainDatasetForStudents')
val_evaluator = dict(
    ignore_index=0, iou_metrics=[
        'mIoU',
        'mDice',
    ], type='IoUMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='Visualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = 'mmsegmentation/practicum_work/artifacts/results/deeplabv3_experiment1'
