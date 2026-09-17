from models import Order, FreelancerProfile
from agent import ResponseAgent

profile = FreelancerProfile(
    name="RobCos",
    specialization="Software Developer",
    skills=["C#", "Java"]
)
order = Order (
    title="Парсер kick.com",
    description="Парсер чата для kick.com. Получает все ники пользователей, которые пишут в чате определенного стримера, " \
    "и сохраняет их в отдельный файл для каждого стримера. " \
    "Также умеет обрабатывать уже записанные стримы по ссылке и извлекать ники из чата. " \
    "После запуска парсера необходимо указать ссылку на стрим, после чего ники сохраняются в новый файл вида kick_ник_стримера.txt.",
    price= 5600,
    currency="RUB"
)
responseAgent = ResponseAgent()
print(responseAgent.build_user_prompt())
 