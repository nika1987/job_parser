from pydantic import BaseModel


class Vacancy(BaseModel):
    id: int
    title: str
    url: str
    payment_from: int | None
    payment_to: int | None
    description: str | None
    city: str | None

    def __lt__(self, other):
        if self.payment_to and other.payment_to:
            return self.payment_to < other.payment_to

    def __gt__(self, other):
        if self.payment_to and other.payment_to:
            return self.payment_to > other.payment_to

