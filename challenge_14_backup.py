#!/usr/bin/env python3

"""
Near Backup Tool
"""

import argparse
import configparser
import tarfile
import os.path
import time


class NearBackup:
    def __init__(self, config_file, args=None):
        self.config_file = config_file
        if not args:
            self.source_dir, self.backup_dir = self.parse_config()
        else:
            self.source_dir = args.source_dir
            self.backup_dir = args.backup_dir

    def parse_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        source_dir = config['SETTINGS']['datadir']
        backup_dir = config['SETTINGS']['backup_dir']
        return source_dir, backup_dir

    def backup(self, output_filename='near_data_backup.tar.gz'):
        filename = f"{self.backup_dir}/{output_filename}"
        with tarfile.open(filename, "w:gz") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))

    def restore(self, source_file='near_data_backup.tar.gz'):
        with tarfile.open(f"{self.backup_dir}/{source_file}") as tar:
            tar.extractall(path=self.source_dir)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-s', '--source', dest='source_dir', type=str, help='Near data directory')
    args.add_argument('-d', '--backup_dir', dest='backup_dir', type=str, help='Backup location')
    args.add_argument('-b', '--backup', dest='backup_operation', action='store_true', help='Perform a backup')
    args.add_argument('-r', '--restore', dest='restore_operation', action='store_true', help='Restore from backup.')
    args = args.parse_args()
    
    api = NearBackup(args=args)
    if args.backup_operation:
        print(f'Backing up the database at {time.time()} ... ')
        api.backup()
    if args.restore_operation:
        print(f'Restoring the database at {time.time()} ... ')
        api.restore()
    
