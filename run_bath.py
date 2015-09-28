#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source import bath


def running_bath(**kwargs):
    bath_obj = bath.Bath(**kwargs)
    bath_obj.run_bath()


def main():
    running_bath(scents=['lavender', 'eucalyptus'])


if __name__ == '__main__':
    main()
