class Menu:
    def get_menu(self):
        return {
            1: {"name": "불고기버거", "price": 5000},
            2: {"name": "치즈버거", "price": 4500},
            3: {"name": "감자튀김", "price": 2000},
            4: {"name": "콜라", "price": 1500}
        }

class Pay:
    def process_payment(self, amount, method):
        print(f"[결제 시스템] {method} 결제 - {amount}원 결제 요청 중...")

        
        if amount >= 20000:  #예: 20000원 이상이면 실패
            print("[결제 시스템] ❌ 결제 실패: 한도 초과")
            return False

        print(f"[결제 시스템] {method} 결제가 완료되었습니다.")
        return True

class Kitchen:
    def print_order(self, order_items, order_type):
        print("[주방 출력기] 주문 내역 전송 중...")
        print(f"※ 주문 방식: {order_type}")
        for item in order_items:
            print(f"- {item['name']} x {item['qty']}")
        print("[주방 출력기] 주문이 접수되었습니다.")

class Kiosk:
    def __init__(self):
        self.menu_system = Menu()
        self.payment_gateway = Pay()
        self.kitchen_printer = Kitchen()
        self.order_type = "매장"

    def choose_order_type(self):
        print("주문 방식을 선택해주세요:")
        print("1. 포장")
        print("2. 매장")
        choice = input("번호 입력: ")
        self.order_type = "포장" if choice == "1" else "매장"
        print(f">> [{self.order_type}] 주문이 선택되었습니다.")

    def start(self):
        print("== 식당 키오스크 ==")
        self.choose_order_type()

        menu = self.menu_system.get_menu()
        order = []

        while True:
            print("\n메뉴를 선택하세요:")
            for num, info in menu.items():
                print(f"{num}. {info['name']} - {info['price']}원")

            try:
                choice = int(input("메뉴 번호 (0 입력 시 종료): "))
                if choice == 0:
                    break
                if choice not in menu:
                    print("잘못된 입력입니다.")
                    continue

                qty = int(input("수량 입력: "))
                if qty <= 0:
                    print("1개 이상 선택해주세요.")
                    continue

                item = menu[choice]
                order.append({"name": item['name'], "price": item['price'], "qty": qty})
            except ValueError:
                print("숫자를 입력해주세요.")

        if not order:
            print("주문이 취소되었습니다.")
            return

        total = sum(item['price'] * item['qty'] for item in order)
        print("\n 주문 내용:")
        for item in order:
            print(f"- {item['name']} x {item['qty']} = {item['price'] * item['qty']}원")
        print(f"총 결제 금액: {total}원")

        print("\n결제 방식을 선택하세요:")
        print("1. 카드")
        print("2. 간편결제")
        print("3. 현금")
        method_choice = input("번호 입력: ")
        method_dict = {"1": "카드", "2": "간편결제", "3": "현금"}

        if method_choice not in method_dict:
            print("유효하지 않은 결제 방식입니다. 주문이 취소되었습니다.")
            return

        method = method_dict[method_choice]

        if self.payment_gateway.process_payment(total, method):
            self.kitchen_printer.print_order(order, self.order_type)
        else:
            print("결제가 실패하여 주문이 완료되지 않았습니다.")

if __name__ == "__main__":
    kiosk = Kiosk()
    kiosk.start()