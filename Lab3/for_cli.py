import argparse
from PikhtovSerLib.create_ser import Choice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serializer of JSON, XML")
    parser.add_argument("file_from", type=str, help="file from which you load data")
    parser.add_argument("file_to", type=str, help="file to which you save serialized data")
    parser.add_argument("format_from", type=str, help="format from which you deserialize data," + \
                                                      "can be any of json/xml")
    parser.add_argument("format_to", type=str, help="format to which you serialize data," + \
                                                    "can be any of json/xml")

    args = parser.parse_args()

    from_serializer = Choice.create_serializer(args.format_from)
    to_serializer = Choice.create_serializer(args.format_to)

    obj = from_serializer.load(args.file_from)

    # print(type(obj), obj)

    to_serializer.dump(obj, args.file_to)
