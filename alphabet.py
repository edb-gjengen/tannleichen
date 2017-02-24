#!/usr/bin/env python
#coding: utf-8
rows = 11
alphabet = [
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\  \  ''',
r'''/:/\:\ \:\__\ ''',
r'''\/__\:\/:/  / ''',
r'''     \::/  /  ''',
r'''     /:/  /   ''',
r'''    /:/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\__\  ''',
r'''/:/\:\ \:|__| ''',
r'''\:\~\:\/:/  / ''',
r''' \:\ \::/  /  ''',
r'''  \:\/:/  /   ''',
r'''   \::/__/    ''',
r'''    ~~        '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /:/  \:\  \  ''',
r'''/:/__/ \:\__\ ''',
r'''\:\  \  \/__/ ''',
r''' \:\  \       ''',
r'''  \:\  \      ''',
r'''   \:\__\     ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /:/  \:\__\  ''',
r'''/:/__/ \:|__| ''',
r'''\:\  \ /:/  / ''',
r''' \:\  /:/  /  ''',
r'''  \:\/:/  /   ''',
r'''   \::/__/    ''',
r'''    ~~        '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\  \  ''',
r'''/:/\:\ \:\__\ ''',
r'''\:\~\:\ \/__/ ''',
r''' \:\ \:\__\   ''',
r'''  \:\ \/__/   ''',
r'''   \:\__\     ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\  \  ''',
r'''/:/\:\ \:\__\ ''',
r'''\/__\:\ \/__/ ''',
r'''     \:\__\   ''',
r'''      \/__/   ''',
r'''              ''',
r'''              '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /:/  \:\  \  ''',
r'''/:/__/_\:\__\ ''',
r'''\:\  /\ \/__/ ''',
r''' \:\ \:\__\   ''',
r'''  \:\/:/  /   ''',
r'''   \::/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /:/  /     ''',
r'''  /:/__/      ''',
r''' /::\  \ ___  ''',
r'''/:/\:\  /\__\ ''',
r'''\/__\:\/:/  / ''',
r'''     \::/  /  ''',
r'''     /:/  /   ''',
r'''    /:/  /    ''',
r'''    \/__/     '''],
[
r'''            ''',
r'''     ___    ''',
r'''    /\  \   ''',
r'''    \:\  \  ''',
r'''    /::\__\ ''',
r''' __/:/\/__/ ''',
r'''/\/:/  /    ''',
r'''\::/__/     ''',
r''' \:\__\     ''',
r'''  \/__/     ''',
r'''            '''],
[
r'''             ''',
r'''      ___    ''',
r'''     /\  \   ''',
r'''     \:\  \  ''',
r''' ___ /::\__\ ''',
r'''/\  /:/\/__/ ''',
r'''\:\/:/  /    ''',
r''' \::/  /     ''',
r'''  \/__/      ''',
r'''             ''',
r'''             '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /:/  /     ''',
r'''  /:/__/      ''',
r''' /::\__\____  ''',
r'''/:/\:::::\__\ ''',
r'''\/_|:|~~|~    ''',
r'''   |:|  |     ''',
r'''   |:|  |     ''',
r'''   |:|  |     ''',
r'''    \|__|     '''],
[
r'''     ___  ''',
r'''    /\__\ ''',
r'''   /:/  / ''',
r'''  /:/  /  ''',
r''' /:/  /   ''',
r'''/:/__/    ''',
r'''\:\  \    ''',
r''' \:\  \   ''',
r'''  \:\  \  ''',
r'''   \:\__\ ''',
r'''    \/__/ '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /::|  |    ''',
r'''  /:|:|  |    ''',
r''' /:/|:|__|__  ''',
r'''/:/ |::::\__\ ''',
r'''\/__/~~/:/  / ''',
r'''      /:/  /  ''',
r'''     /:/  /   ''',
r'''    /:/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /::|  |    ''',
r'''  /:|:|  |    ''',
r''' /:/|:|  |__  ''',
r'''/:/ |:| /\__\ ''',
r'''\/__|:|/:/  / ''',
r'''    |:/:/  /  ''',
r'''    |::/  /   ''',
r'''    /:/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /:/  \:\  \  ''',
r'''/:/__/ \:\__\ ''',
r'''\:\  \ /:/  / ''',
r''' \:\  /:/  /  ''',
r'''  \:\/:/  /   ''',
r'''   \::/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\  \  ''',
r'''/:/\:\ \:\__\ ''',
r'''\/__\:\/:/  / ''',
r'''     \::/  /  ''',
r'''      \/__/   ''',
r'''              ''',
r'''              '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r'''  \:\~\:\  \  ''',
r'''   \:\ \:\__\ ''',
r'''    \:\/:/  / ''',
r'''     \::/  /  ''',
r'''     /:/  /   ''',
r'''    /:/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\:\  \   ''',
r''' /::\~\:\  \  ''',
r'''/:/\:\ \:\__\ ''',
r'''\/_|::\/:/  / ''',
r'''   |:|::/  /  ''',
r'''   |:|\/__/   ''',
r'''   |:|  |     ''',
r'''    \|__|     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''   /::\  \    ''',
r'''  /:/\ \  \   ''',
r''' _\:\~\ \  \  ''',
r'''/\ \:\ \ \__\ ''',
r'''\:\ \:\ \/__/ ''',
r''' \:\ \:\__\   ''',
r'''  \:\/:/  /   ''',
r'''   \::/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''    \:\  \    ''',
r'''     \:\  \   ''',
r'''     /::\  \  ''',
r'''    /:/\:\__\ ''',
r'''   /:/  \/__/ ''',
r'''  /:/  /      ''',
r'''  \/__/       ''',
r'''              ''',
r'''              '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /:/  /     ''',
r'''  /:/  /      ''',
r''' /:/  /  ___  ''',
r'''/:/__/  /\__\ ''',
r'''\:\  \ /:/  / ''',
r''' \:\  /:/  /  ''',
r'''  \:\/:/  /   ''',
r'''   \::/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /:/  /     ''',
r'''  /:/  /      ''',
r''' /:/__/  ___  ''',
r''' |:|  | /\__\ ''',
r''' |:|  |/:/  / ''',
r''' |:|__/:/  /  ''',
r'''  \::::/__/   ''',
r'''   ~~~~       ''',
r'''              '''],
[
r'''     ___      ''',
r'''    /\__\     ''',
r'''   /:/ _/_    ''',
r'''  /:/ /\__\   ''',
r''' /:/ /:/ _/_  ''',
r'''/:/_/:/ /\__\ ''',
r'''\:\/:/ /:/  / ''',
r''' \::/_/:/  /  ''',
r'''  \:\/:/  /   ''',
r'''   \::/  /    ''',
r'''    \/__/     '''],
[
r'''     ___      ''',
r'''    |\__\     ''',
r'''    |:|  |    ''',
r'''    |:|  |    ''',
r'''    |:|__|__  ''',
r'''____/::::\__\ ''',
r'''\::::/~~/~    ''',
r''' ~~|:|~~|     ''',
r'''   |:|  |     ''',
r'''   |:|  |     ''',
r'''    \|__|     '''],
[
r'''     ___      ''',
r'''    |\__\     ''',
r'''    |:|  |    ''',
r'''    |:|  |    ''',
r'''    |:|__|__  ''',
r'''    /::::\__\ ''',
r'''   /:/~~/~    ''',
r'''  /:/  /      ''',
r'''  \/__/       ''',
r'''              ''',
r'''              '''],
[
r'''     ___      ''',
r'''    /\  \     ''',
r'''    \:\  \    ''',
r'''     \:\  \   ''',
r'''      \:\  \  ''',
r'''_______\:\__\ ''',
r'''\::::::::/__/ ''',
r''' \:\~~\~~     ''',
r'''  \:\  \      ''',
r'''   \:\__\     ''',
r'''    \/__/     ''']
]
