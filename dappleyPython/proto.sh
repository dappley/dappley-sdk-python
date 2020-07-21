# build.sh
python -m grpc_tools.protoc -I ./proto --python_out=lib/protobuf --grpc_python_out=lib/protobuf ./proto/*.proto
