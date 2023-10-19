from collections import Counter

from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from applications.users.permissions import is_any_editor_or_superuser


def send_email(subject, html_content, from_email, to_emails):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content)

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))  # Imprime el mensaje de error


def filter_and_sort_projects(projects, user):
    # Filtrar estados según el grupo del usuario
    if is_any_editor_or_superuser(user):
        allowed_statuses = ["Incompleto", "Pendiente"]
    else:
        allowed_statuses = ["Incompleto", "Pendiente", "Rechazado"]

    # Filtrar proyectos
    filtered_projects = [project for project in projects if
                         project.application_status in allowed_statuses]

    # Contar los proyectos
    status_list = [project.application_status for project in filtered_projects]
    counters = Counter(status_list)
    total_count = sum(counters.values())

    # Ordenar proyectos
    if is_any_editor_or_superuser(user):
        sorted_projects = sorted(
            filtered_projects,
            key=lambda x: (x.application_status == "Pendiente", x.modified_date),
            reverse=True
        )[:3]
    else:
        order_values = {"Pendiente": 1, "Rechazado": 2, "Incompleto": 3}
        sorted_projects = sorted(
            filtered_projects,
            key=lambda x: (order_values.get(x.application_status, 4), x.modified_date),
            reverse=True
        )[:3]

    return total_count, sorted_projects