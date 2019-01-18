import os
from lxml import etree
from PIL import Image

class XMLCropper:

    def __init__(self, xml_path):
        self.tree = etree.parse(xml_path)
        self.data = self._parse()

    def _parse(self):
        result = {
            'folder':   self.tree.find('folder').text,
            'filename': self.tree.find('filename').text,
            'path':     self.tree.find('path').text,
            'items':    [],
        }
        for obj in self.tree.xpath('/annotation/object'):
            bndbox = obj.find('bndbox')
            item = {
                'label':    obj.find('name').text,
                'xmin':     int(bndbox.find('xmin').text),
                'ymin':     int(bndbox.find('ymin').text),
                'xmax':     int(bndbox.find('xmax').text),
                'ymax':     int(bndbox.find('ymax').text),
            }
            result['items'].append(item)
        return result

    def _crop(self, idx, label, box, dest_dir):
        img = Image.open(self.data['path'])
        crop = img.crop(box)
        ff = self.data['filename'].split('.')
        dest_path = os.path.join(dest_dir, "%s_%02d_%s.%s" % ( ff[0], idx+1, label, ff[1] ))
        #print(dest_path)
        crop.save(dest_path, quality=100)

    def crop(self, dest_dir):
        for idx, item in enumerate(self.data['items']):
            box = ( item['xmin'], item['ymin'], item['xmax'], item['ymax'] )
            self._crop(idx, item['label'], box, dest_dir)

if __name__ == "__main__":

    import sys
    from pprint import pprint as pp

    xml_path = sys.argv[1]
    out_path = sys.argv[2]

    cropper = XMLCropper(xml_path)
    cropper.crop(out_path)
