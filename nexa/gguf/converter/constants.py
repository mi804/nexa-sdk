from nexa.gguf.llama.llama_cpp import (
    LLAMA_FTYPE_ALL_F32,
    LLAMA_FTYPE_MOSTLY_F16,
    LLAMA_FTYPE_MOSTLY_Q4_0,
    LLAMA_FTYPE_MOSTLY_Q4_1,
    LLAMA_FTYPE_MOSTLY_Q8_0,
    LLAMA_FTYPE_MOSTLY_Q5_0,
    LLAMA_FTYPE_MOSTLY_Q5_1,
    LLAMA_FTYPE_MOSTLY_Q2_K,
    LLAMA_FTYPE_MOSTLY_Q3_K_S,
    LLAMA_FTYPE_MOSTLY_Q3_K_M,
    LLAMA_FTYPE_MOSTLY_Q3_K_L,
    LLAMA_FTYPE_MOSTLY_Q4_K_S,
    LLAMA_FTYPE_MOSTLY_Q4_K_M,
    LLAMA_FTYPE_MOSTLY_Q5_K_S,
    LLAMA_FTYPE_MOSTLY_Q5_K_M,
    LLAMA_FTYPE_MOSTLY_Q6_K,
    LLAMA_FTYPE_MOSTLY_IQ2_XXS,
    LLAMA_FTYPE_MOSTLY_IQ2_XS,
    LLAMA_FTYPE_MOSTLY_Q2_K_S,
    LLAMA_FTYPE_MOSTLY_IQ3_XS,
    LLAMA_FTYPE_MOSTLY_IQ3_XXS,
    LLAMA_FTYPE_MOSTLY_IQ1_S,
    LLAMA_FTYPE_MOSTLY_IQ4_NL,
    LLAMA_FTYPE_MOSTLY_IQ3_S,
    LLAMA_FTYPE_MOSTLY_IQ3_M,
    LLAMA_FTYPE_MOSTLY_IQ2_S,
    LLAMA_FTYPE_MOSTLY_IQ2_M,
    LLAMA_FTYPE_MOSTLY_IQ4_XS,
    LLAMA_FTYPE_MOSTLY_IQ1_M,
    LLAMA_FTYPE_MOSTLY_BF16,
    LLAMA_FTYPE_MOSTLY_Q4_0_4_4,
    LLAMA_FTYPE_MOSTLY_Q4_0_4_8,
    LLAMA_FTYPE_MOSTLY_Q4_0_8_8,
    LLAMA_FTYPE_MOSTLY_TQ1_0,
    LLAMA_FTYPE_MOSTLY_TQ2_0,
)
from nexa.gguf.llama.llama_cpp import (
    GGML_TYPE_F32,
    GGML_TYPE_F16,
    GGML_TYPE_Q4_0,
    GGML_TYPE_Q4_1,
    GGML_TYPE_Q5_0,
    GGML_TYPE_Q5_1,
    GGML_TYPE_Q8_0,
    GGML_TYPE_Q8_1,
    GGML_TYPE_Q2_K,
    GGML_TYPE_Q3_K,
    GGML_TYPE_Q4_K,
    GGML_TYPE_Q5_K,
    GGML_TYPE_Q6_K,
    GGML_TYPE_Q8_K,
    GGML_TYPE_IQ2_XXS,
    GGML_TYPE_IQ2_XS,
    GGML_TYPE_IQ3_XXS,
    GGML_TYPE_IQ1_S,
    GGML_TYPE_IQ4_NL,
    GGML_TYPE_IQ3_S,
    GGML_TYPE_IQ2_S,
    GGML_TYPE_IQ4_XS,
    GGML_TYPE_I8,
    GGML_TYPE_I16,
    GGML_TYPE_I32,
    GGML_TYPE_I64,
    GGML_TYPE_F64,
    GGML_TYPE_IQ1_M,
    GGML_TYPE_BF16,
    GGML_TYPE_Q4_0_4_4,
    GGML_TYPE_Q4_0_4_8,
    GGML_TYPE_Q4_0_8_8,
    GGML_TYPE_COUNT,
)

# From quantize.cpp
# For mapping of general quantization options (ftypes)
LLAMA_QUANTIZATION_TYPES = {
    "q4_0": LLAMA_FTYPE_MOSTLY_Q4_0,
    "q4_1": LLAMA_FTYPE_MOSTLY_Q4_1,
    "q5_0": LLAMA_FTYPE_MOSTLY_Q5_0,
    "q5_1": LLAMA_FTYPE_MOSTLY_Q5_1,
    "q8_0": LLAMA_FTYPE_MOSTLY_Q8_0,
    "q2_k": LLAMA_FTYPE_MOSTLY_Q2_K,
    "q3_k_s": LLAMA_FTYPE_MOSTLY_Q3_K_S,
    "q3_k_m": LLAMA_FTYPE_MOSTLY_Q3_K_M,
    "q3_k_l": LLAMA_FTYPE_MOSTLY_Q3_K_L,
    "q4_k_s": LLAMA_FTYPE_MOSTLY_Q4_K_S,
    "q4_k_m": LLAMA_FTYPE_MOSTLY_Q4_K_M,
    "q5_k_s": LLAMA_FTYPE_MOSTLY_Q5_K_S,
    "q5_k_m": LLAMA_FTYPE_MOSTLY_Q5_K_M,
    "q6_k": LLAMA_FTYPE_MOSTLY_Q6_K,
    "iq2_xxs": LLAMA_FTYPE_MOSTLY_IQ2_XXS,
    "iq2_xs": LLAMA_FTYPE_MOSTLY_IQ2_XS,
    "q2_k_s": LLAMA_FTYPE_MOSTLY_Q2_K_S,
    "iq3_xs": LLAMA_FTYPE_MOSTLY_IQ3_XS,
    "iq3_xxs": LLAMA_FTYPE_MOSTLY_IQ3_XXS,
    "iq1_s": LLAMA_FTYPE_MOSTLY_IQ1_S,
    "iq4_nl": LLAMA_FTYPE_MOSTLY_IQ4_NL,
    "iq3_s": LLAMA_FTYPE_MOSTLY_IQ3_S,
    "iq3_m": LLAMA_FTYPE_MOSTLY_IQ3_M,
    "iq2_s": LLAMA_FTYPE_MOSTLY_IQ2_S,
    "iq2_m": LLAMA_FTYPE_MOSTLY_IQ2_M,
    "iq4_xs": LLAMA_FTYPE_MOSTLY_IQ4_XS,
    "iq1_m": LLAMA_FTYPE_MOSTLY_IQ1_M,
    "f16": LLAMA_FTYPE_MOSTLY_F16,
    "f32": LLAMA_FTYPE_ALL_F32,
    "bf16": LLAMA_FTYPE_MOSTLY_BF16,
    "q4_0_4_4": LLAMA_FTYPE_MOSTLY_Q4_0_4_4,
    "q4_0_4_8": LLAMA_FTYPE_MOSTLY_Q4_0_4_8,
    "q4_0_8_8": LLAMA_FTYPE_MOSTLY_Q4_0_8_8,
    "tq1_0": LLAMA_FTYPE_MOSTLY_TQ1_0,
    "tq2_0": LLAMA_FTYPE_MOSTLY_TQ2_0,
}

# From ggml.h
# For mapping of output_tensor_type and token_embedding_type only
GGML_TYPES = {
    "f32": GGML_TYPE_F32,
    "f16": GGML_TYPE_F16,
    "q4_0": GGML_TYPE_Q4_0,
    "q4_1": GGML_TYPE_Q4_1,
    "q5_0": GGML_TYPE_Q5_0,
    "q5_1": GGML_TYPE_Q5_1,
    "q8_0": GGML_TYPE_Q8_0,
    "q8_1": GGML_TYPE_Q8_1,
    "q2_k": GGML_TYPE_Q2_K,
    "q3_k": GGML_TYPE_Q3_K,
    "q4_k": GGML_TYPE_Q4_K,
    "q5_k": GGML_TYPE_Q5_K,
    "q6_k": GGML_TYPE_Q6_K,
    "q8_k": GGML_TYPE_Q8_K,
    "iq2_xxs": GGML_TYPE_IQ2_XXS,
    "iq2_xs": GGML_TYPE_IQ2_XS,
    "iq3_xxs": GGML_TYPE_IQ3_XXS,
    "iq1_s": GGML_TYPE_IQ1_S,
    "iq4_nl": GGML_TYPE_IQ4_NL,
    "iq3_s": GGML_TYPE_IQ3_S,
    "iq2_s": GGML_TYPE_IQ2_S,
    "iq4_xs": GGML_TYPE_IQ4_XS,
    "i8": GGML_TYPE_I8,
    "i16": GGML_TYPE_I16,
    "i32": GGML_TYPE_I32,
    "i64": GGML_TYPE_I64,
    "f64": GGML_TYPE_F64,
    "iq1_m": GGML_TYPE_IQ1_M,
    "bf16": GGML_TYPE_BF16,
    "q4_0_4_4": GGML_TYPE_Q4_0_4_4,
    "q4_0_4_8": GGML_TYPE_Q4_0_4_8,
    "q4_0_8_8": GGML_TYPE_Q4_0_8_8,
}