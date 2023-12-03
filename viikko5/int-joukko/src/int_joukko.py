class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.ljono += self._luo_lista(self.kasvatuskoko)

            return True

        return False

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos_joukko = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            tulos_joukko.lisaa(luku)
        return tulos_joukko

    @staticmethod
    def leikkaus(a, b):
        tulos_joukko = IntJoukko()
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                tulos_joukko.lisaa(luku)
        return tulos_joukko

    @staticmethod
    def erotus(a, b):
        tulos_joukko = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                tulos_joukko.lisaa(luku)
        return tulos_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
