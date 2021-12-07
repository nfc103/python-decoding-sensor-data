from house_info import HouseInfo

class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS=0x0F0

    def _get_energy(self,rec):
        energy = int(rec,base=16)
        energy = energy & ENERGY_BITS
        energy = energy >> 4
        return energy
