# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 00:36:24 2016

@author: yl
"""

class Dex(object):
    """
    
    """
    def __init__(self, pokemon_names):
        """Constructor

        GameObject.__init__(Dex, list of str)
        """
        # ↓ 1.命名规范：class 内的 private attribute 用 _开头
        #     数据用一个dic存储即可
        self._pokemon_dic = {}
        for pokemon in pokemon_names:
            self._pokemon_dic[pokemon] = 0

    def expect_pokemons(self, pokemon_names):
        """Method

        GameObject.expect_pokemons(Dex, list of str)
        """
        for pokemon in pokemon_names:
            if pokemon not in self._pokemon_dic: 
            # ↑ 2.判断 pokemon 是否在 dic 里
            # ↓ 3.若不在 则 将 dic 内对应的 key 设为 0 
                self._pokemon_dic[pokemon] = 0 
    
    def __str__(self):
        pass
        
            
            
        self._pokemon_names = pokemon_names









