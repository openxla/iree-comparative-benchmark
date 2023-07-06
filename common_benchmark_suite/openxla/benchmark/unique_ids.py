# Copyright 2023 The OpenXLA Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""List of unique IDs in the benchmark suite.

Each ID should start with a UUID generated from uuid.uuid4().
"""

################################################################################
# T5 models                                                                    #
################################################################################
MODEL_IMPL_T5 = "173c7180-bad4-4b91-8423-4beeb13d2b0a-MODEL_IMPL"
MODEL_T5_LARGE = "173c7180-bad4-4b91-8423-4beeb13d2b0a-MODEL_T5_LARGE"
MODEL_T5_LARGE_FP32 = f"{MODEL_T5_LARGE}-fp32"
MODEL_T5_LARGE_FP16 = f"{MODEL_T5_LARGE}-fp16"
MODEL_T5_LARGE_BF16 = f"{MODEL_T5_LARGE}-bf16"

# JAX T5 Large models and test data.
MODEL_IMPL_T5_JAX = f"{MODEL_IMPL_T5}-JAX"

MODEL_T5_LARGE_FP32_JAX = f"{MODEL_T5_LARGE_FP32}-JAX"
MODEL_T5_LARGE_FP16_JAX = f"{MODEL_T5_LARGE_FP16}-JAX"
MODEL_T5_LARGE_BF16_JAX = f"{MODEL_T5_LARGE_BF16}-JAX"

MODEL_T5_LARGE_FP32_JAX_512XI32 = f"{MODEL_T5_LARGE_FP32_JAX}-512xi32"
MODEL_T5_LARGE_FP16_JAX_512XI32 = f"{MODEL_T5_LARGE_FP16_JAX}-512xi32"
MODEL_T5_LARGE_BF16_JAX_512XI32 = f"{MODEL_T5_LARGE_BF16_JAX}-512xi32"

INPUT_DATA_T5_LARGE_JAX_512 = "4552b15b-8d90-498c-9282-f6553ae4db38"
INPUT_DATA_T5_LARGE_FP32_JAX_512XI32 = f"{INPUT_DATA_T5_LARGE_JAX_512}-fp32"
INPUT_DATA_T5_LARGE_FP16_JAX_512XI32 = f"{INPUT_DATA_T5_LARGE_JAX_512}-fp16"
INPUT_DATA_T5_LARGE_BF16_JAX_512XI32 = f"{INPUT_DATA_T5_LARGE_JAX_512}-bf16"
OUTPUT_DATA_T5_LARGE_JAX_512X1024 = "e245bd97-a1fa-4f35-b04b-92664c4f49db"
OUTPUT_DATA_T5_LARGE_FP32_JAX_512X1024XF32 = f"{OUTPUT_DATA_T5_LARGE_JAX_512X1024}-fp32"
OUTPUT_DATA_T5_LARGE_FP16_JAX_512X1024XF16 = f"{OUTPUT_DATA_T5_LARGE_JAX_512X1024}-fp16"
OUTPUT_DATA_T5_LARGE_BF16_JAX_512X1024XBF16 = f"{OUTPUT_DATA_T5_LARGE_JAX_512X1024}-bf16"

# JAX T5ForConditionalGeneration models and test data.
# Note: `4CG` is short for `ForConditionalGeneration`.
MODEL_IMPL_T5_4CG = "1dd120bd-fa12-4d26-9f84-92a8c8f50d1e-MODEL_IMPL"
MODEL_T5_4CG_LARGE = "1dd120bd-fa12-4d26-9f84-92a8c8f50d1e-MODEL_T5_4CG_LARGE"
MODEL_T5_4CG_LARGE_FP32 = f"{MODEL_T5_4CG_LARGE}-fp32"

MODEL_IMPL_T5_4CG_JAX = f"{MODEL_IMPL_T5_4CG}-JAX"

MODEL_T5_4CG_LARGE_FP32_JAX = f"{MODEL_T5_4CG_LARGE_FP32}-JAX"

INPUT_DATA_T5_4CG_LARGE_JAX_512XI32 = "49de56f6-a3d2-4b25-abc1-0a922f0affec"
INPUT_DATA_T5_4CG_LARGE_FP32_JAX_512XI32 = f"{INPUT_DATA_T5_4CG_LARGE_JAX_512XI32}-fp32"

OUTPUT_DATA_T5_4CG_LARGE_JAX_512X1024 = "49eb591d-4d91-4b16-94bf-7d01cda3826b"
OUTPUT_DATA_T5_4CG_LARGE_FP32_JAX_512X1024XF32 = f"{OUTPUT_DATA_T5_4CG_LARGE_JAX_512X1024}-fp32"

# TF T5 Large models and test data.
MODEL_IMPL_T5_TF = f"{MODEL_IMPL_T5}-TF"

MODEL_T5_LARGE_FP32_TF = f"{MODEL_T5_LARGE_FP32}-TF"
MODEL_T5_LARGE_FP32_TF_512XI32 = f"{MODEL_T5_LARGE_FP32_TF}-512xi32"

INPUT_DATA_T5_LARGE_TF_512XI32 = "0e4c9be9-15b7-4cae-aa71-a912d3abe0f5"
INPUT_DATA_T5_LARGE_FP32_TF_512XI32 = f"{INPUT_DATA_T5_LARGE_TF_512XI32}-fp32"

OUTPUT_DATA_T5_LARGE_TF_512X1024XF32 = "c72052c0-85b0-49f2-b875-ca3e5031b0df"
OUTPUT_DATA_T5_LARGE_FP32_TF_512X1024XF32 = f"{OUTPUT_DATA_T5_LARGE_TF_512X1024XF32}-fp32"

################################################################################
# Bert models                                                                  #
################################################################################
MODEL_BERT = "47cb0d3a-5eb7-41c7-9d7c-97aae7023ecf"
MODEL_BERT_LARGE = f"{MODEL_BERT}-MODEL_BERT_LARGE"
MODEL_BERT_LARGE_FP32 = f"{MODEL_BERT_LARGE}-fp32"
MODEL_BERT_LARGE_FP16 = f"{MODEL_BERT_LARGE}-fp16"
MODEL_BERT_LARGE_BF16 = f"{MODEL_BERT_LARGE}-bf16"

# JAX BERT models and test data.
MODEL_IMPL_BERT_JAX = f"{MODEL_BERT}-MODEL_IMPL-JAX"

MODEL_BERT_LARGE_FP32_JAX = f"{MODEL_BERT_LARGE_FP32}-JAX"
MODEL_BERT_LARGE_FP32_JAX_384XI32 = f"{MODEL_BERT_LARGE_FP32_JAX}-384xi32"

MODEL_BERT_LARGE_FP16_JAX = f"{MODEL_BERT_LARGE_FP16}-JAX"
MODEL_BERT_LARGE_FP16_JAX_384XI32 = f"{MODEL_BERT_LARGE_FP16_JAX}-384xi32"

MODEL_BERT_LARGE_BF16_JAX = f"{MODEL_BERT_LARGE_BF16}-JAX"
MODEL_BERT_LARGE_BF16_JAX_384XI32 = f"{MODEL_BERT_LARGE_BF16_JAX}-384xi32"

INPUT_DATA_BERT_LARGE_JAX_384XI32 = "4ba707a4-1de7-4bc8-a9f6-b40b04af503d"
INPUT_DATA_BERT_LARGE_FP32_JAX_384XI32 = f"{INPUT_DATA_BERT_LARGE_JAX_384XI32}-fp32"
INPUT_DATA_BERT_LARGE_FP16_JAX_384XI32 = f"{INPUT_DATA_BERT_LARGE_JAX_384XI32}-fp16"
INPUT_DATA_BERT_LARGE_BF16_JAX_384XI32 = f"{INPUT_DATA_BERT_LARGE_JAX_384XI32}-bf16"
OUTPUT_DATA_BERT_LARGE_JAX_384X1024 = "dce6c4a4-0fc3-43d6-bb01-b818331cdbd3"
OUTPUT_DATA_BERT_LARGE_FP32_JAX_384X1024XF32 = f"{OUTPUT_DATA_BERT_LARGE_JAX_384X1024}-fp32"
OUTPUT_DATA_BERT_LARGE_FP16_JAX_384X1024XF16 = f"{OUTPUT_DATA_BERT_LARGE_JAX_384X1024}-fp16"
OUTPUT_DATA_BERT_LARGE_BF16_JAX_384X1024XBF16 = f"{OUTPUT_DATA_BERT_LARGE_JAX_384X1024}-bf16"

# TF BERT models and test data.
MODEL_IMPL_BERT_TF = f"{MODEL_BERT}-MODEL_IMPL-TF"

MODEL_BERT_LARGE_FP32_TF = f"{MODEL_BERT_LARGE_FP32}-TF"
MODEL_BERT_LARGE_FP32_TF_384XI32 = f"{MODEL_BERT_LARGE_FP32_TF}-384xi32"

INPUT_DATA_BERT_LARGE_TF_384XI32 = "824428d8-e0cc-4611-83b8-91939a300725"
INPUT_DATA_BERT_LARGE_FP32_TF_384XI32 = f"{INPUT_DATA_BERT_LARGE_TF_384XI32}-fp32"

OUTPUT_DATA_BERT_LARGE_TF_384X1024 = "73ecdf68-46b5-4f8f-b2ec-2a182857642d"
OUTPUT_DATA_BERT_LARGE_FP32_TF_384X1024XF32 = f"{OUTPUT_DATA_BERT_LARGE_TF_384X1024}-fp32"

# PT Bert models.
MODEL_IMPL_BERT_PT = f"{MODEL_BERT}-MODEL_IMPL-PT"

MODEL_BERT_LARGE_FP32_PT = f"{MODEL_BERT_LARGE_FP32}-PT"
MODEL_BERT_LARGE_FP32_PT_384XI32 = f"{MODEL_BERT_LARGE_FP32_PT}-384xi32"

MODEL_BERT_LARGE_FP16_PT = f"{MODEL_BERT_LARGE_FP16}-PT"
MODEL_BERT_LARGE_FP16_PT_384XI32 = f"{MODEL_BERT_LARGE_FP16_PT}-384xi32"

INPUT_DATA_BERT_LARGE_PT_384XI32 = "2bbb87cf-a910-4262-a9d8-ceff295f1c24"
INPUT_DATA_BERT_LARGE_FP32_PT_384XI32 = f"{INPUT_DATA_BERT_LARGE_PT_384XI32}-fp32"
INPUT_DATA_BERT_LARGE_FP16_PT_384XI32 = f"{INPUT_DATA_BERT_LARGE_PT_384XI32}-fp16"

OUTPUT_DATA_BERT_LARGE_PT_384X1024 = "cd625ba7-fc70-4a87-92eb-5acab0c77beb"
OUTPUT_DATA_BERT_LARGE_FP32_PT_384X1024XF32 = f"{OUTPUT_DATA_BERT_LARGE_PT_384X1024}-fp32"
OUTPUT_DATA_BERT_LARGE_FP16_PT_384X1024XF16 = f"{OUTPUT_DATA_BERT_LARGE_PT_384X1024}-fp16"

################################################################################
# ResNet models                                                                #
################################################################################
MODEL_IMPL_RESNET = "aff75509-4420-40a8-844e-dbfc48494fe6-MODEL_IMPL"
MODEL_RESNET50 = "aff75509-4420-40a8-844e-dbfc48494fe6-MODEL_RESNET50"
MODEL_RESNET50_FP32 = f"{MODEL_RESNET50}-fp32"
MODEL_RESNET50_FP16 = f"{MODEL_RESNET50}-fp16"
MODEL_RESNET50_BF16 = f"{MODEL_RESNET50}-bf16"

# JAX ResNet models and test data.
MODEL_IMPL_RESNET_JAX = f"{MODEL_IMPL_RESNET}-JAX"
MODEL_RESNET50_FP32_JAX = f"{MODEL_RESNET50_FP32}-JAX"
MODEL_RESNET50_FP16_JAX = f"{MODEL_RESNET50_FP16}-JAX"
MODEL_RESNET50_BF16_JAX = f"{MODEL_RESNET50_BF16}-JAX"

MODEL_RESNET50_FP32_JAX_3X224X224XF32 = f"{MODEL_RESNET50_FP32_JAX}-3x224x224xf32"
MODEL_RESNET50_FP16_JAX_3X224X224XF16 = f"{MODEL_RESNET50_FP16_JAX}-3x224x224xf16"
MODEL_RESNET50_BF16_JAX_3X224X224XBF16 = f"{MODEL_RESNET50_BF16_JAX}-3x224x224xbf16"

INPUT_DATA_RESNET50_FP32_JAX_3X224X224 = "b2676fcd-1cc1-4b79-84a2-71c7efaeb58b"
INPUT_DATA_RESNET50_FP32_JAX_3X224X224XF32 = f"{INPUT_DATA_RESNET50_FP32_JAX_3X224X224}-fp32"
INPUT_DATA_RESNET50_FP16_JAX_3X224X224XF16 = f"{INPUT_DATA_RESNET50_FP32_JAX_3X224X224}-fp16"
INPUT_DATA_RESNET50_BF16_JAX_3X224X224XBF16 = f"{INPUT_DATA_RESNET50_FP32_JAX_3X224X224}-bf16"
OUTPUT_DATA_RESNET50_FP32_JAX_2048X7X7 = "33b967bb-302c-47a9-bb20-f0834f4d3838"
OUTPUT_DATA_RESNET50_FP32_JAX_2048X7X7XF32 = f"{OUTPUT_DATA_RESNET50_FP32_JAX_2048X7X7}-fp32"
OUTPUT_DATA_RESNET50_FP16_JAX_2048X7X7XF16 = f"{OUTPUT_DATA_RESNET50_FP32_JAX_2048X7X7}-fp16"
OUTPUT_DATA_RESNET50_BF16_JAX_2048X7X7XBF16 = f"{OUTPUT_DATA_RESNET50_FP32_JAX_2048X7X7}-bf16"

# TF ResNet models and test data.
MODEL_IMPL_RESNET_TF = f"{MODEL_IMPL_RESNET}-TF"

MODEL_RESNET50_FP32_TF = f"{MODEL_RESNET50_FP32}-TF"
MODEL_RESNET50_FP32_TF_3X224X224XF32 = f"{MODEL_RESNET50_FP32_TF}-224x224x3xf32"

INPUT_DATA_RESNET50_TF_3X224X224 = "b2676fcd-1cc1-4b79-84a2-71c7efaeb58b"
INPUT_DATA_RESNET50_FP32_TF_3X224X224XF32 = f"{INPUT_DATA_RESNET50_TF_3X224X224}-fp32"

OUTPUT_DATA_RESNET50_TF_2048X7X7 = "33b967bb-302c-47a9-bb20-f0834f4d3838"
OUTPUT_DATA_RESNET50_FP32_TF_2048X7X7XF32 = f"{OUTPUT_DATA_RESNET50_TF_2048X7X7}-fp32"


################################################################################
# Device IDs                                                                   #
################################################################################
DEVICE_SPEC_GCP_C2_STANDARD_16 = "9a4804f1-b1b9-46cd-b251-7f16a655f782"
DEVICE_SPEC_GCP_A2_HIGHGPU_1G = "78c56b95-2d7d-44b5-b5fd-8e47aa961108"
