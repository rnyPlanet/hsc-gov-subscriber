import asyncio

from subscriber.services.hsc_gov_subscriber import HscGovSubscriber

if __name__ == '__main__':
    text = """🎫 Знайдено талони 🏛️ ТСЦ МВС № 4841 м. Миколаїв, пров. Транспортний, 1а/1
    💼 На послугу: 🚗 Практичний іспит (транспортний засіб навчального закладу)
    ✅ Талони наявні на наступні дати :
    📆 2.5.2024 - 1 🎫 талон
    📆 30.4.2024 - 1 🎫 талон 
    📆 30.9.2024 - 1 🎫 талон 
    """

    # asyncio.run(HscGovSubscriber().subscribe(text))
