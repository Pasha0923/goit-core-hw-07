from address_book import AddressBook
from models import Record
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            msg = str(e).lower() 
            if "unpack" in msg or "too many values" in msg or "not enough" in msg: 
                return "❌ Please provide the correct number of arguments"
            return f"❌ {e}"
        except KeyError:
            return "❌ This contact does not exist"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner
    
def parse_input(user_input: str) -> tuple:
    """
    Parses user input into command and arguments.
    Args:
        user_input (str): input string from user.
    Returns:
        tuple: (command, args)
    """
    parts = user_input.strip().split()
    if not parts:
        return '', []
    return parts[0].lower(), parts[1:]


@input_error
def add_contact(args, book: AddressBook):
    # args: ["John", "1234567890"]
    name, phone, *_ = args  
    record = book.find(name)  
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    # args: ["John", "1234567890", "0987654321"]
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "Phone number updated."


@input_error
def show_phone(args, book: AddressBook):
    # args: ["John"]
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if not record.phones:
        return "No phone numbers found for this contact."
    phones = ', '.join(phone.value for phone in record.phones)
    return f"Phone numbers for {name}: {phones}"


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "AddressBook is empty."
    result = []
    for record in book.data.values():
        phones = ', '.join(phone.value for phone in record.phones) if record.phones else "No phone numbers"
        result.append(f"{record.name.value}: {phones}")
    return "\n".join(result)

@input_error
def add_birthday(args, book: AddressBook):
    # args: ["John", "01.01.1990"]
    name, birthday_str = args
    record = book.find(name)
    if record is None:
        return "❌ Contact not found"
    record.add_birthday(birthday_str)
    return f"Birthday for {name} to {birthday_str}"


@input_error
def show_birthday(args, book: AddressBook):
    # args: ["John"]
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "❌ Contact not found"
    if not record.birthday:
        return f"No birthday set for {name}"
    return f"{name}'s birthday is: {record.birthday.value}"

@input_error
def birthdays(book: AddressBook):
    """Обробника для команди 'birthdays' - показує імена та дні народження користувачів, у яких дні народження протягом наступних 7 днів"""
    upcoming = book.get_upcoming_birthdays(days=7)
    if isinstance(upcoming, str):
        return upcoming 
    return "\n".join(f"{u['name']}: {u['birthday']}" for u in upcoming)