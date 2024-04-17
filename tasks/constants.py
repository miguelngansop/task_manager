from enum import Enum


class ErrorMessage:
    # Error messages for validation
    INVALID_IMPORTANCE = 'Invalid importance value. Please choose from "Low", "Medium", or "High".'
    REQUIRED_FIELD = 'This field is required. Please provide a value.'
    INVALID_TITLE = 'Please enter a valid title. The title should be between 1 and 200 characters long.'
    INVALID_DESCRIPTION = 'Please enter a valid description. The description should be less than 2000 characters long.'
    INVALID_DUE_DATE = 'Please enter a valid due date. The date should be in the format YYYY-MM-DD HH:MM:SS.'
    INVALID_CREATED_BY = 'Please enter a valid creator.'
    # Add more user-friendly error messages with instructions as needed for other fields

class Importance(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'