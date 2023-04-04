from enum import Enum


class ResponseCode(Enum):
    ERROR_CODE_GENERIC = "ERR_COMMON_001"
    USER_NOT_FOUND = "ERR_REG_002"
    MERCHANT_NOT_FOUND = "Merchant_Not_Found"
    CLIENT_NOT_FOUND = "Client_Not_Found"
    PRODUCT_NOT_FOUND = "Product_Not_Found"
    SERVICE_NOT_FOUND = "Service_Not_Found"
    MORE_THAN_ONE_RECORD_FOUND = "More_Than_One_Record_Found"
    SUCCESS = "Success"
    FAILURE = "Failure"
    ADDED_SUCCESSFULLY = "Added_Successfully"
    UPDATED_SUCCESSFULLY = "Updated Successfully"
    SUBSCRIBED = "Subscribed"
    UNSUBSCRIBED = "Unsubscribed"
    UNSUBSCRIBED_SUCCESSFULLY = "Unsubscribed"
    FIELD_EMPTY = "Can't be blank"
    RECORD_NOT_FOUND = "Record Not Found"
    CUSTOMER_EXISTS = "Customer exists"
    MOBILE_NUMBER_EXISTS = "Mobile_Number_exists"
    EMAIL_EXISTS = "Email_exists"
    CUSTOMER_NOT_FOUND = "Customer Not Found"
    CUSTOMER_CLIENT_COMBINATION_EXISTS = "Customer Client Combintion Exists"
    NORMAL_CLIENT = "Normal Client"
    PARENT_CLIENT = "Parent client"
    CHILD_CLIENT = "Child client"
    CUSTOMER_TYPE = "Customer"
    ID_PATTERN = "[0-9]"
    NO_CHNAGES_FOUND = "No changes found"
    EMAIL_PATTERN = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@" + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
    REFERRAL_CLIENT = "Referral"
    MERCHANT = "Merchant"