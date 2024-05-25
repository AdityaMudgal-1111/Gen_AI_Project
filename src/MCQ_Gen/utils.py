import os
import json
import traceback
import PyPDF2


def read_file():
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text =+ page.extract_text()
            return text
        except exception as e:
            raise Exception("error reading the PDF file")

    elif file.name.endswith(".txt"):
        return file.read().decode('utf-8')

    else:
        raise Exception("unsupported file format, only pdf and txt file are supported")

def get_table_data():
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value['mcq']
            options = " || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value['options'] in items()
                ]
            )
            correct = value['correct']
            quiz_table_data.append({'MCQ' : mcq, "choice": option, "correct": correct})

        return quiz_table_data

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except KeyError as e:
        print(f"Missing key in quiz data: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
        

