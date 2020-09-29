from enum import Enum
from typing import NamedTuple


class Events(Enum):
    DATA = 'scraper:data'
    END = 'scraper:end'
    ERROR = 'scraper:error'


class Data(NamedTuple):
    query: str = ''
    location: str = ''
    link: str = ''
    apply_link: str = ''
    title: str = ''
    company: str = ''
    place: str = ''
    description: str = ''
    description_html: str = ''
    date: str = ''
    senority_level: str = ''
    job_function: str = ''
    employment_type: str = ''
    industries: str = ''