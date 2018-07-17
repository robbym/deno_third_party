# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASYNC_GENERATOR_REQUEST_TYPE",
  159: "DEBUG_INFO_TYPE",
  160: "FUNCTION_TEMPLATE_INFO_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_INFO_ENTRY_TYPE",
  164: "MODULE_TYPE",
  165: "OBJECT_TEMPLATE_INFO_TYPE",
  166: "PROMISE_CAPABILITY_TYPE",
  167: "PROMISE_REACTION_TYPE",
  168: "PROTOTYPE_INFO_TYPE",
  169: "SCRIPT_TYPE",
  170: "STACK_FRAME_INFO_TYPE",
  171: "TUPLE2_TYPE",
  172: "TUPLE3_TYPE",
  173: "WASM_DEBUG_INFO_TYPE",
  174: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  175: "CALLABLE_TASK_TYPE",
  176: "CALLBACK_TASK_TYPE",
  177: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  178: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  179: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  180: "ALLOCATION_SITE_TYPE",
  181: "FIXED_ARRAY_TYPE",
  182: "BOILERPLATE_DESCRIPTION_TYPE",
  183: "HASH_TABLE_TYPE",
  184: "ORDERED_HASH_MAP_TYPE",
  185: "ORDERED_HASH_SET_TYPE",
  186: "NAME_DICTIONARY_TYPE",
  187: "GLOBAL_DICTIONARY_TYPE",
  188: "NUMBER_DICTIONARY_TYPE",
  189: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  190: "STRING_TABLE_TYPE",
  191: "EPHEMERON_HASH_TABLE_TYPE",
  192: "SCOPE_INFO_TYPE",
  193: "SCRIPT_CONTEXT_TABLE_TYPE",
  194: "BLOCK_CONTEXT_TYPE",
  195: "CATCH_CONTEXT_TYPE",
  196: "DEBUG_EVALUATE_CONTEXT_TYPE",
  197: "EVAL_CONTEXT_TYPE",
  198: "FUNCTION_CONTEXT_TYPE",
  199: "MODULE_CONTEXT_TYPE",
  200: "NATIVE_CONTEXT_TYPE",
  201: "SCRIPT_CONTEXT_TYPE",
  202: "WITH_CONTEXT_TYPE",
  203: "WEAK_FIXED_ARRAY_TYPE",
  204: "DESCRIPTOR_ARRAY_TYPE",
  205: "TRANSITION_ARRAY_TYPE",
  206: "CALL_HANDLER_INFO_TYPE",
  207: "CELL_TYPE",
  208: "CODE_DATA_CONTAINER_TYPE",
  209: "FEEDBACK_CELL_TYPE",
  210: "FEEDBACK_VECTOR_TYPE",
  211: "LOAD_HANDLER_TYPE",
  212: "PROPERTY_ARRAY_TYPE",
  213: "PROPERTY_CELL_TYPE",
  214: "SHARED_FUNCTION_INFO_TYPE",
  215: "SMALL_ORDERED_HASH_MAP_TYPE",
  216: "SMALL_ORDERED_HASH_SET_TYPE",
  217: "STORE_HANDLER_TYPE",
  218: "WEAK_CELL_TYPE",
  219: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1076: "JS_SET_TYPE",
  1077: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1078: "JS_SET_VALUE_ITERATOR_TYPE",
  1079: "JS_STRING_ITERATOR_TYPE",
  1080: "JS_WEAK_MAP_TYPE",
  1081: "JS_WEAK_SET_TYPE",
  1082: "JS_TYPED_ARRAY_TYPE",
  1083: "JS_DATA_VIEW_TYPE",
  1084: "JS_INTL_LOCALE_TYPE",
  1085: "WASM_GLOBAL_TYPE",
  1086: "WASM_INSTANCE_TYPE",
  1087: "WASM_MEMORY_TYPE",
  1088: "WASM_MODULE_TYPE",
  1089: "WASM_TABLE_TYPE",
  1090: "JS_BOUND_FUNCTION_TYPE",
  1091: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x02201): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x02259): (132, "MetaMap"),
  ("RO_SPACE", 0x022e1): (131, "NullMap"),
  ("RO_SPACE", 0x02359): (204, "DescriptorArrayMap"),
  ("RO_SPACE", 0x023c1): (181, "FixedArrayMap"),
  ("RO_SPACE", 0x02429): (218, "WeakCellMap"),
  ("RO_SPACE", 0x024d1): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x02539): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x025d1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x02661): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x02721): (131, "UndefinedMap"),
  ("RO_SPACE", 0x02799): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x02831): (131, "TheHoleMap"),
  ("RO_SPACE", 0x028f9): (131, "BooleanMap"),
  ("RO_SPACE", 0x02a09): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x02a71): (181, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x02ad9): (183, "HashTableMap"),
  ("RO_SPACE", 0x02b41): (128, "SymbolMap"),
  ("RO_SPACE", 0x02ba9): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x02c11): (192, "ScopeInfoMap"),
  ("RO_SPACE", 0x02c79): (214, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x02ce1): (133, "CodeMap"),
  ("RO_SPACE", 0x02d49): (198, "FunctionContextMap"),
  ("RO_SPACE", 0x02db1): (207, "CellMap"),
  ("RO_SPACE", 0x02e19): (213, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x02e81): (135, "ForeignMap"),
  ("RO_SPACE", 0x02ee9): (205, "TransitionArrayMap"),
  ("RO_SPACE", 0x02f51): (210, "FeedbackVectorMap"),
  ("RO_SPACE", 0x02ff9): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x030b9): (131, "ExceptionMap"),
  ("RO_SPACE", 0x03179): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x03241): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x03301): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x03391): (200, "NativeContextMap"),
  ("RO_SPACE", 0x033f9): (199, "ModuleContextMap"),
  ("RO_SPACE", 0x03461): (197, "EvalContextMap"),
  ("RO_SPACE", 0x034c9): (201, "ScriptContextMap"),
  ("RO_SPACE", 0x03531): (194, "BlockContextMap"),
  ("RO_SPACE", 0x03599): (195, "CatchContextMap"),
  ("RO_SPACE", 0x03601): (202, "WithContextMap"),
  ("RO_SPACE", 0x03669): (196, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x036d1): (193, "ScriptContextTableMap"),
  ("RO_SPACE", 0x03739): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x037a1): (181, "ArrayListMap"),
  ("RO_SPACE", 0x03809): (130, "BigIntMap"),
  ("RO_SPACE", 0x03871): (182, "BoilerplateDescriptionMap"),
  ("RO_SPACE", 0x038d9): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x03941): (208, "CodeDataContainerMap"),
  ("RO_SPACE", 0x039a9): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x03a11): (187, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x03a79): (209, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x03ae1): (181, "ModuleInfoMap"),
  ("RO_SPACE", 0x03b49): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x03bb1): (186, "NameDictionaryMap"),
  ("RO_SPACE", 0x03c19): (209, "NoClosuresCellMap"),
  ("RO_SPACE", 0x03c81): (188, "NumberDictionaryMap"),
  ("RO_SPACE", 0x03ce9): (209, "OneClosureCellMap"),
  ("RO_SPACE", 0x03d51): (184, "OrderedHashMapMap"),
  ("RO_SPACE", 0x03db9): (185, "OrderedHashSetMap"),
  ("RO_SPACE", 0x03e21): (212, "PropertyArrayMap"),
  ("RO_SPACE", 0x03e89): (206, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x03ef1): (206, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03f59): (206, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03fc1): (189, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x04029): (181, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x04091): (215, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x040f9): (216, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x04161): (190, "StringTableMap"),
  ("RO_SPACE", 0x041c9): (203, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x04231): (219, "WeakArrayListMap"),
  ("RO_SPACE", 0x04299): (191, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x04301): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x04369): (64, "StringMap"),
  ("RO_SPACE", 0x043d1): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x04439): (65, "ConsStringMap"),
  ("RO_SPACE", 0x044a1): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x04509): (69, "ThinStringMap"),
  ("RO_SPACE", 0x04571): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x045d9): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x04641): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x046a9): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04711): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x04779): (98, "ShortExternalStringMap"),
  ("RO_SPACE", 0x047e1): (114, "ShortExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04849): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x048b1): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x04919): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04981): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x049e9): (34, "ShortExternalInternalizedStringMap"),
  ("RO_SPACE", 0x04a51): (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04ab9): (42, "ShortExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x04b21): (106, "ShortExternalOneByteStringMap"),
  ("RO_SPACE", 0x04b89): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x04bf1): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x04c59): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x04cc1): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x04d29): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x04d91): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x04df9): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x04e61): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x04ec9): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x04f31): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x04f99): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x05001): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x05081): (171, "Tuple2Map"),
  ("RO_SPACE", 0x053c9): (161, "InterceptorInfoMap"),
  ("RO_SPACE", 0x054e9): (169, "ScriptMap"),
  ("RO_SPACE", 0x09dc1): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x09fd1): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x0a039): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x0a0a1): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x0a109): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x0a171): (158, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x0a1d9): (159, "DebugInfoMap"),
  ("RO_SPACE", 0x0a241): (160, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x0a2a9): (162, "InterpreterDataMap"),
  ("RO_SPACE", 0x0a311): (163, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x0a379): (164, "ModuleMap"),
  ("RO_SPACE", 0x0a3e1): (165, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x0a449): (166, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x0a4b1): (167, "PromiseReactionMap"),
  ("RO_SPACE", 0x0a519): (168, "PrototypeInfoMap"),
  ("RO_SPACE", 0x0a581): (170, "StackFrameInfoMap"),
  ("RO_SPACE", 0x0a5e9): (172, "Tuple3Map"),
  ("RO_SPACE", 0x0a651): (173, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x0a6b9): (174, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x0a721): (175, "CallableTaskMap"),
  ("RO_SPACE", 0x0a789): (176, "CallbackTaskMap"),
  ("RO_SPACE", 0x0a7f1): (177, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x0a859): (178, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x0a8c1): (179, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x0a929): (180, "AllocationSiteMap"),
  ("RO_SPACE", 0x0a991): (180, "AllocationSiteMap"),
  ("MAP_SPACE", 0x02201): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x02259): (1072, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x022b1): "NullValue",
  ("RO_SPACE", 0x02339): "EmptyDescriptorArray",
  ("RO_SPACE", 0x023b1): "EmptyFixedArray",
  ("RO_SPACE", 0x025a1): "UninitializedValue",
  ("RO_SPACE", 0x026f1): "UndefinedValue",
  ("RO_SPACE", 0x02789): "NanValue",
  ("RO_SPACE", 0x02801): "TheHoleValue",
  ("RO_SPACE", 0x028b9): "HoleNanValue",
  ("RO_SPACE", 0x028c9): "TrueValue",
  ("RO_SPACE", 0x029a1): "FalseValue",
  ("RO_SPACE", 0x029f1): "empty_string",
  ("RO_SPACE", 0x02fb9): "EmptyScopeInfo",
  ("RO_SPACE", 0x02fc9): "ArgumentsMarker",
  ("RO_SPACE", 0x03089): "Exception",
  ("RO_SPACE", 0x03149): "TerminationException",
  ("RO_SPACE", 0x03211): "OptimizedOut",
  ("RO_SPACE", 0x032d1): "StaleRegister",
  ("RO_SPACE", 0x050f9): "EmptyByteArray",
  ("RO_SPACE", 0x05119): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x05139): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x05159): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x05179): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x05199): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x051b9): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x051d9): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x051f9): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x05219): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x05279): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x05299): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x052e1): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x05309): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x05341): "EmptyPropertyCell",
  ("RO_SPACE", 0x05369): "EmptyWeakCell",
  ("RO_SPACE", 0x05459): "InfinityValue",
  ("RO_SPACE", 0x05469): "MinusZeroValue",
  ("RO_SPACE", 0x05479): "MinusInfinityValue",
  ("RO_SPACE", 0x05489): "SelfReferenceMarker",
  ("OLD_SPACE", 0x02211): "EmptyScript",
  ("OLD_SPACE", 0x02299): "ManyClosuresCell",
  ("OLD_SPACE", 0x022b9): "NoElementsProtector",
  ("OLD_SPACE", 0x022e1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x022f1): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x02319): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x02341): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x02369): "StringLengthProtector",
  ("OLD_SPACE", 0x02379): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x023a1): "ArrayBufferNeuteringProtector",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.