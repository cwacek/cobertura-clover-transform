import lxml.etree as ET
import argparse
import pkg_resources


def convert(inxml):

    dom = ET.parse(inxml)
    xslt = ET.parse(pkg_resources.resource_stream('cobertura_clover_transform',
                                                  'transform.xslt'))

    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    return ET.tostring(newdom, pretty_print=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('coverage_xml')
    args = parser.parse_args()

    converted = convert(args.coverage_xml)

    print(converted)
