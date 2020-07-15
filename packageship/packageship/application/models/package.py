#!/usr/bin/python3
"""
Description: Database entity model mapping
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from packageship.libs.dbutils.sqlalchemy_helper import DBHelper


class src_pack(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
        Source package model
    """

    __tablename__ = 'src_pack'

    pkgKey = Column(Integer, primary_key=True)
    pkgId = Column(String(500), nullable=True)
    name = Column(String(200), nullable=True)
    arch = Column(String(200), nullable=True)
    version = Column(String(500), nullable=True)
    epoch = Column(String(200), nullable=True)
    release = Column(String(500), nullable=True)
    summary = Column(String(500), nullable=True)
    description = Column(String(500), nullable=True)
    url = Column(String(500), nullable=True)
    time_file = Column(Integer, nullable=True)
    time_build = Column(Integer, nullable=True)
    rpm_license = Column(String(500), nullable=True)
    rpm_vendor = Column(String(500), nullable=True)
    rpm_group = Column(String(500), nullable=True)
    rpm_buildhost = Column(String(500), nullable=True)
    rpm_sourcerpm = Column(String(500), nullable=True)
    rpm_header_start = Column(Integer, nullable=True)
    rpm_header_end = Column(Integer, nullable=True)
    rpm_packager = Column(String(500), nullable=True)
    size_package = Column(Integer, nullable=True)
    size_installed = Column(Integer, nullable=True)
    size_archive = Column(Integer, nullable=True)
    location_href = Column(String(500), nullable=True)
    location_base = Column(String(500), nullable=True)
    checksum_type = Column(String(500), nullable=True)


class bin_pack(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
    Description: functional description:Binary package data
    """
    __tablename__ = 'bin_pack'

    pkgKey = Column(Integer, primary_key=True)
    pkgId = Column(String(500), nullable=True)
    name = Column(String(500), nullable=True)
    arch = Column(String(500), nullable=True)
    version = Column(String(500), nullable=True)
    epoch = Column(String(500), nullable=True)
    release = Column(String(500), nullable=True)
    summary = Column(String(500), nullable=True)
    description = Column(String(500), nullable=True)
    url = Column(String(500), nullable=True)
    time_file = Column(Integer, nullable=True)
    time_build = Column(Integer, nullable=True)
    rpm_license = Column(String(500), nullable=True)
    rpm_vendor = Column(String(500), nullable=True)
    rpm_group = Column(String(500), nullable=True)
    rpm_buildhost = Column(String(500), nullable=True)
    rpm_sourcerpm = Column(String(500), nullable=True)
    rpm_header_start = Column(Integer, nullable=True)
    rpm_header_end = Column(Integer, nullable=True)
    rpm_packager = Column(String(500), nullable=True)
    size_package = Column(Integer, nullable=True)
    size_installed = Column(Integer, nullable=True)
    size_archive = Column(Integer, nullable=True)
    location_href = Column(String(500), nullable=True)
    location_base = Column(String(500), nullable=True)
    checksum_type = Column(String(500), nullable=True)
    src_name = Column(String(500), nullable=True)


class bin_requires(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
        Binary package dependent package entity model
    """

    __tablename__ = 'bin_requires'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)
    flags = Column(String(200), nullable=True)
    epoch = Column(String(200), nullable=True)
    version = Column(String(500), nullable=True)
    release = Column(String(200), nullable=True)
    pkgKey = Column(Integer, nullable=True)
    pre = Column(String(20), nullable=True)


class src_requires(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
        Source entity package dependent package entity model
    """
    __tablename__ = 'src_requires'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)
    flags = Column(String(200), nullable=True)
    epoch = Column(String(200), nullable=True)
    version = Column(String(500), nullable=True)
    release = Column(String(200), nullable=True)
    pkgKey = Column(Integer, nullable=True)
    pre = Column(String(20), nullable=True)


class bin_provides(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
        Component entity model provided by binary package
    """
    __tablename__ = 'bin_provides'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)
    flags = Column(String(200), nullable=True)
    epoch = Column(String(200), nullable=True)
    version = Column(String(500), nullable=True)
    release = Column(String(200), nullable=True)
    pkgKey = Column(Integer, nullable=True)


class maintenance_info(DBHelper.BASE):  # pylint: disable=C0103,R0903
    """
        Maintain data related to person information
    """
    __tablename__ = 'maintenance_info'

    id = Column(Integer, primary_key=True)

    name = Column(String(500), nullable=True)

    version = Column(String(500), nullable=True)

    maintaniner = Column(String(100), nullable=True)

    maintainlevel = Column(String(100), nullable=True)
