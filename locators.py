#Locators for all Gemini tests
#
#


class HomePageLocator(object):
    #Exchange Gemini Home Page (exchange.sandbox.gemini.com)
    createAccountLink = "//a[@href='/register']"


class RegisterPageLocator(object):
    #Exchange Gemini Register Page (https://exchange.sandbox.gemini.com/register)
    cookieOkButton = "a.e5i1odf0.css-1h8byj3"
    createBusinessLink = "//a[@href='/register/institution']"


class InstitutionPageLocator(object):
    #Exchange Gemini Register Institution Page (https://exchange.sandbox.gemini.com/register/institution)
    businessNameInput = "company.legalName"
    companyTypeDropdown = "div[class='companyTypeDropdown__placeholder css-13u7ap5-placeholder']"
    companyTypeSelection = "react-select-2-option-0"
    stateTypeDropdown = "div[class='usStateDropdown__placeholder css-13u7ap5-placeholder']"
    stateTypeSelection = "react-select-4-option-0"
    firstNameInput = "personal.legalName.firstName"
    middleNameInput = "personal.legalName.middleName"
    lastNameInput = "personal.legalName.lastName"
    emailInput = "personal.email"
    continueButton = "button.e5i1odf0.css-bpqdh4"
    errorAlert = "div[class='Alert error']"


class SuccessPageLocator(object):
    #Exchange Gemini Register Institution Success Page (https://exchange.sandbox.gemini.com/register/institution/thanks)
    successPageBody = "body[class='page-body SuccessPage']"
