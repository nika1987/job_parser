from constants import HH_URL, SUPERJOB_URL, DATA_FILE
from managers.file_storage import FileStorage
from managers.headhunter import HeadHunterAPI
from managers.service import VacancyService
from managers.superjob import SuperJobAPI

hh_managers = HeadHunterAPI(HH_URL)
superjob_manager = SuperJobAPI(SUPERJOB_URL)
filestore_manager = FileStorage(DATA_FILE)
vacancy_service = VacancyService(hh_managers, superjob_manager, filestore_manager)
