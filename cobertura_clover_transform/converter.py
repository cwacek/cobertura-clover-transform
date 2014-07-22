import lxml.etree as ET
import argparse
import pkgutil


def convert(inxml):

    dom = ET.parse(inxml)
    xslt = ET.parse(pkgutil.resource_stream('cobertura-clover-transform',
                                            'transform.xslt'))

    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    return ET.tostring(newdom, pretty_print=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('coverage-xml')
    args = parser.parse_args()

    converted = convert(args.coverage_xml)
