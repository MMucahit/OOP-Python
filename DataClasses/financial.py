from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Stock:
    ticker: str
    price: int
    dividend: float = field(default=0)
    dividend_frequency: int = field(default=4)

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency

@dataclass(order=True)
class Position:
    stock: Stock = field(compare=False)
    shares: int = field(compare=True)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Position):
            return False
        
        return self.stock.price * self.shares == __value.stock.price * __value.shares

@dataclass
class Portfolio:
    holdings: List[Position]

    @property
    def value(self):
        result = sum([position.stock.price * position.shares for position in self.holdings])
        return result
    
    @property
    def portfolio_yield(self):
        result = sum([position.stock.annual_dividend * position.shares for position in self.holdings]) / self.value
        return round(result, 6)

if __name__ == '__main__':
    MSFT = Stock('MSFT', 320, 0.62, 4)
    LMT = Stock('LMT', 320, 3.2, 4)
    GOOGLE = Stock('GOOGLE', 2800, 0, 0)

    p1 = Position(MSFT, 100)
    p2 = Position(LMT, 100)
    p3 = Position(GOOGLE, 10)

    portfolio = Portfolio(holdings=[p1, p2, p3])

    print(MSFT.annual_dividend, LMT.annual_dividend, GOOGLE.annual_dividend)
    print(p1, p2, p3, p1 == p2)
    print(portfolio.value, portfolio.portfolio_yield)