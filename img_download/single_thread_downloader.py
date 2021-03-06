import logging
import os
from time import time

from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(threadName)s|%(message)s')
log = logging.getLogger(__name__)

if __name__ == '__main__':
	ts = time()

	client_id = os.getenv('IMGUR_CLIENT_ID')
	if not client_id:
		raise Exception("Couldn't find IMGUR_CLIENT_ID env variable")

	download_dir = setup_download_dir()
	links = get_links(client_id)
	for link in links:
		download_link(download_dir, link)

	log.info('Took %s seconds', time() - ts)