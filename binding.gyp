{
   "targets": [{
      "sources": ["sleep.cxx"],
      "target_name": "sleep",
      "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
   }]
}
