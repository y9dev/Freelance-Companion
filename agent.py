from models import Order, FreelancerProfile
from prompts import SYSTEM_PROMPT

# This .py code takes the Order, the Profile and the System prompt into account.
# The agent then sends the results it made further to the LLM.

class ResponseAgent:
    def build_user_prompt(
    self,
    order: Order,
    profile: FreelancerProfile
) -> str:
        return ("ORDER \n"
      f"Title: {order.title} \n"
      f"Description: {order.description} \n"
      f"Price: {order.price} \n"
      f"Payment Currency: {order.currency}")