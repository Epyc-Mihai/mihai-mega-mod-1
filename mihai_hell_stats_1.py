import ctx as ctx
import discord


class StatsMod:
    def __init__(self, capital: str, name: str, nationality: str, country: str, updated: int, uuid: int, flag: str,
                 created: str, lan: int, pop: int, factory: int, land: int, emp: str, rank: str, score: float,
                 competitiveRank: str, gdp: str, balance: str, currency: str, coinz: str, tech: str, keys: str,
                 badge1: str, badge2: str, badge3: str):
        self.country = country
        self.updated = updated
        self.uuid = uuid
        self.flag = flag
        self.created = created
        self.lan = lan
        self.pop = pop
        self.factory = factory
        self.land = land
        self.emp = emp
        self.rank = rank
        self.score = score
        self.competitiveRank = competitiveRank
        self.gdp = gdp
        self.balance = balance
        self.currency = currency
        self.coinz = coinz
        self.tech = tech
        self.keys = keys
        self.badge1 = badge1
        self.badge2 = badge2
        self.badge3 = badge3
        self.capital = capital
        self.nationality = nationality
        self.name = name


def UserMod(self):
    embed = discord.Embed(title="<:bar_chart:956998752156123147> Statistics", color=0x00ff00)

    embed.set_image(url=self.flag)

    embed.add_field(name="<:name_badge:956992653780729906> Name", value=f"{(self.name)}", inline=False)
    embed.add_field(name="<:calendar:957004169888292934> Founded On", value=f"{(self.created)}", inline=False)
    embed.add_field(name="<:crown:956999150128496650> Leader",
                    value=f"{(ctx.author.mention)} | "f"{(self.uuid)} | "f"{(self.rank)}", inline=False)
    embed.add_field(name="<:watch:956991718266396712> Updated", value=f"{(self.updated)}", inline=False)
    embed.add_field(name="<:beginner:956991593678770207> Badges",
                    value=f"{(self.badge1)} | "f"{(self.badge2)} | "f"{(self.badge3)} |", inline=False)
    embed.add_field(name="<:trophy:956992508431314944> Competitive Rank",
                    value=f"{(self.competitiveRank)} | {(self.score)}", inline=False)
    embed.add_field(name="<:crossed_flags:956988222901194772> Empire", value=f"{(self.emp)}", inline=False)
    embed.add_field(name="<:dollar:956989950291771474> Currency", value=f"{(self.currency)}", inline=False)
    embed.add_field(name="<:money_with_wings:956989643373555812> Gross Domestic Product", value=f"{(self.gdp)}",
                    inline=False)
    embed.add_field(name="<:moneybag:956988715698376754> Balance", value=f"{(self.balance)}", inline=False)
    embed.add_field(name="<:coin:956988470331576390> Coinz", value=f"{(self.coinz)}", inline=False)
    embed.add_field(name="<:factory:956991820565475398> Processors", value=f"{(self.factory)}", inline=False)
    embed.add_field(name="<:flag_white:956994631311167558> Nationality", value=f"{(self.nationality)}", inline=False)
    embed.add_field(name="<:cityscape:956994804259115108> Capital City", value=f"{(self.capital)}", inline=False)
    embed.add_field(name="<:key2:956994431167385670> Keys", value=f"{(self.keys)}", inline=False)
    embed.add_field(name="<:man:956990682336227348> Country Population", value=f"{(self.pop)}", inline=False)
    embed.add_field(name="<:homes:956995223697883167> Land Area", value=f"{(self.lan)}", inline=False)
    embed.add_field(name="<:test_tube:957004559547519046> Technology Points", value=f"{(self.tech)}", inline=False)
    embed.add_field(name="<:park:956995020458696736> Free Land Area", value=f"{(self.land)}", inline=False)
    embed.set_footer(text="My nuts, hang, and, add, @everyone.")

    return embed