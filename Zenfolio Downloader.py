import os
import re

import requests
import zenapi


_dir_root = '~/Downloads/ZenfolioBackup'


def process_gallery(gallery, curr_dir):
  gallery = zen.LoadPhotoSet(
      gallery.Id, level=zenapi._zapi.InformationLevel.Level2, includePhotos=True)
  for photo in gallery.Photos:
    if photo.IsVideo:
      continue
    fp = os.path.join(curr_dir, photo.FileName)
    if not os.path.exists(fp):
      headers = {'X-Zenfolio-Token': zen.auth}
      response = requests.get(photo.OriginalUrl, headers=headers, stream=True)
      if response.status_code == 200:
        with open(fp, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)


def process_group(group, curr_dir):
  for element in group.Elements:
    dir_name = re.sub(r'[/\\:*?""<>|]', '_', element.Title)
    dir = os.path.join(curr_dir, dir_name)
    if isinstance(element, zenapi._zapi.Group):
      process_group(element, dir)
      continue

    # Download physical galleries only. Collections are skipped.
    if element.Type == 'Gallery':
      if not os.path.exists(dir):
        os.makedirs(dir)
      process_gallery(element, dir)


if __name__ == '__main__':
  zen = zenapi.ZenConnection(username='info@wendyhilliardfoundation.org', password='Whfgymnastics123123')
  zen.Authenticate()
  root = zen.LoadGroupHierarchy()
  process_group(root, _dir_root)