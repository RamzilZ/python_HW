from Address import Address
from Mailing import Mailing
to_Address = Address ("125424", "Moscow", "Sovetskaya Street", "9", "9")
from_Address = Address ("461758", "Orenburg", "Gagarina avenue", "26", "7")
mailing = Mailing(to_Address == to_Address, from_Address == from_Address, cost=4, track=20260930)
track_info = f"Отправление {mailing.track} из"
from_info = f"{from_Address.__formatted_address__()}"
to_info = f" в {to_Address.__formatted_address__()}"
cost_info = f" . Стоимость {mailing.cost} рублей. "
print (track_info + from_info + to_info + cost_info
       )
