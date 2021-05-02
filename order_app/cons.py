# Responses
DATA = 'data'
ERRORS = 'errors'
VALID = 'valid'
MESSAGE = 'message'
FILTER_PREFIX = 'flt_'
ERROR_TYPE = 'type'

VALIDATION_ERROR = 'ValidationError'
HTTP_404 = 'Http404'
HTTP_400 = 'Http400'
HTTP_401 = 'Http401'
HTTP_403 = 'Http403'
INTEGRITY_ERROR = 'IntegrityError'
OTHER = 'Other'
FIELD_ERROR = 'FieldError'
INVALID_DATA = 'InvalidData'
UNAUTHORIZED = 'Unauthorized'
EMAIL_ERROR = 'EmailError'
ERROR_MESSAGE = 'error_message'
#
# GROUP_ADMINISTRATOR = 'Administrator'
# GROUP_SECTOR_HEAD = 'Përgjegjës sektori'
# GROUP_DEPARTMENT_HEAD = 'Përgjegjës njësie bazë'
# GROUP_SPECIALIST = 'Specialist'
# GROUP_FINANCE = 'Financë'
# GROUP_ACCEPTANCE = 'Zyrë pranimi'
#
# # Content type id
# STRUCTURE_DEPARTMENT = 9
# STRUCTURE_SECTOR = 11
# STRUCTURE_LABORATORY = 10
#
# STRUCTURES = {
#     STRUCTURE_DEPARTMENT: 'Departament',
#     STRUCTURE_SECTOR: 'Sektor',
#     STRUCTURE_LABORATORY: 'Laborator'
# }
#
# PHYSICAL_CHEMICAL = 1
# MICROBIOLOGICAL = 2
#
# ANALYTE_TYPE = {
#     PHYSICAL_CHEMICAL: 'Fiziko-Kimik',
#     MICROBIOLOGICAL: 'Mikrobiologjik',
# }
#
# SECTOR_CONSIGNOR = 1
# SUBJECT_CONSIGNOR = 2
# VKSH_CONSIGNOR = 3
# QSUT_CONSIGNOR = 4
# ISHP_CONSIGNOR = 5
# INDIVID_CONSIGNOR = 6
# OTHER_CONSIGNOR = 7
#
# CONSIGNOR_TYPE = {
#     SECTOR_CONSIGNOR: 'SEKTORI',
#     SUBJECT_CONSIGNOR: 'SUBJEKTI',
#     VKSH_CONSIGNOR: 'VKSH',
#     QSUT_CONSIGNOR: 'QSUT',
#     ISHP_CONSIGNOR: 'ISHP',
#     INDIVID_CONSIGNOR: 'INDIVID',
#     OTHER_CONSIGNOR: 'TJETËR'
#
# }
#
# GENDER_MALE = 0
# GENDER_FEMALE = 1
# GENDER_CHOICES = {
#     GENDER_MALE: 'Mashkull',
#     GENDER_FEMALE: 'Femer'
# }
#
# #  Acceptance sheet
#
# REDACTION_ACCEPTANCE = 1
# WAITING_PAYMENT_ACCEPTANCE = 2
# PUBLISHED_ACCEPTANCE = 3
# REFUSED_ACCEPTANCE = 4
#
# ACCEPTANCE_SHEET_STATES = {
#     REDACTION_ACCEPTANCE: 'Redaktim',
#     WAITING_PAYMENT_ACCEPTANCE: 'Në pritje të pagesës',
#     PUBLISHED_ACCEPTANCE: 'Publikuar',
#     REFUSED_ACCEPTANCE: 'Refuzuar'
# }
#
# PUBLISH_DEBIT = 1
# PUBLISH_PAID = 2
#
# #  Laboratory sheet
#
# REDACTION_LABORATORY_SHEET = 1
# PUBLISHED_LABORATORY_SHEET = 2
# REJECTED_LABORATORY_SHEET = 3
#
# LABORATORY_SHEET_STATES = {
#     REDACTION_LABORATORY_SHEET: 'Redaktim',
#     PUBLISHED_LABORATORY_SHEET: 'Publikuar',
#     REJECTED_LABORATORY_SHEET: 'Refuzuar',
# }
#
#
# def reportlab_text(string):
#     return string.replace('&', '&amp;')
#
#
# def get_validation_error_message(error_data):
#     try:
#         response_message = ''
#         if isinstance(error_data, dict):
#             for key, value in error_data.items():
#                 for item in value:
#                     if 'message' in item:
#                         response_message += '{}: {} '.format(key, item['message'])
#                     else:
#                         if isinstance(item, dict):
#                             for unit_key, unit_value in item.items():
#                                 for arr_item in unit_value:
#                                     response_message += '{}: {} '.format(unit_key, arr_item['message'])
#                         elif isinstance(item, str):
#                             for item_key, item_val in value.items():
#                                 for arr_item in item_val:
#                                     response_message += '{}: {} '.format(item_key, arr_item['message'])
#         elif isinstance(error_data, list):
#             for arr_item in error_data:
#                 response_message += '{} '.format(arr_item['message'])
#     except:
#         response_message = 'Error {}'.format(error_data)
#     return response_message
#
#
# class EagerLoadingMixin:
#     @classmethod
#     def setup_eager_loading(cls, queryset):
#         if hasattr(cls, "SELECT_RELATED"):
#             queryset = queryset.select_related(*cls.SELECT_RELATED)
#         if hasattr(cls, "PREFETCH_RELATED"):
#             queryset = queryset.prefetch_related(*cls.PREFETCH_RELATED)
#         return queryset
