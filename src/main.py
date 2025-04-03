import streamlit as st


def main():
    st.title("P2P Calculator")

    # Default platform configuration
    platform = {
        'name': 'Binance',
        'buy_currency': 'USD',
        'you_will_pay': 0,
        'buying_rate': 0,
        'sell_currency': 'BDT',
        'selling_rate': 0,
        'intermediate_currency': 'USDT',
        'processing_fee': 0.05
    }

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"{platform['name']} - Buy")
        platform['buy_currency'] = st.selectbox("Buying Currency", ["USD", "GBP", "EUR", "BDT"], index=0)
        platform['you_will_pay'] = st.number_input("You will pay", min_value=0.0, format="%.2f")
        platform['buying_rate'] = st.number_input("Buying rate", min_value=0.0, format="%.3f")
        receivable_usdt = calculate_receivable_usdt(platform)
        st.text(f"Receivable {platform['intermediate_currency']}: {receivable_usdt:.2f}")
        st.caption(f"Processing fee applied: {platform['processing_fee']:.2f} {platform['intermediate_currency']}")

    with col2:
        st.subheader(f"{platform['name']} - Sell")
        platform['sell_currency'] = st.selectbox("Selling Currency", ["USD", "GBP", "EUR", "BDT"], index=0)
        platform['selling_rate'] = st.number_input("Selling rate", min_value=0.0, format="%.2f")
        you_will_receive = calculate_you_will_receive(platform, receivable_usdt)
        st.text(f"You will receive: {you_will_receive:.2f}")
        st.caption(f"Processing fee applied: {platform['processing_fee']:.2f} {platform['intermediate_currency']}")

def calculate_receivable_usdt(platform):
    return (platform['you_will_pay'] - platform['processing_fee']) / platform['buying_rate'] if platform['buying_rate'] > 0 else 0

def calculate_you_will_receive(platform, total_amount):
    convertible_amount = (total_amount - platform['processing_fee'])
    return (platform['selling_rate'] * convertible_amount)

if __name__ == "__main__":
    main()