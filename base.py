def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def main():
    print("=== Calculadora de Divisas ===")
    try:
        budget = float(input("Ingresa el presupuesto en USD: "))
        exchange_rate = float(input("Ingresa la tasa de cambio (1 moneda local = X USD): "))
        
        resultado = exchange_money(budget, exchange_rate)
        print(f"\nCon {budget} USD obtienes {resultado:.2f} en moneda local.")
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa solo números.")

if __name__ == "__main__":
    main()

# === Ejemplos probados ===
# Japón: exchange_money(300, 0.0075) → 40000.0
# Alemania: exchange_money(300, 1.08) → 277.78
# Canadá: exchange_money(300, 0.73) → 410.96
