
G = 6.67430e-11  # м^3·с^-2·кг^-1 (или Н·м²·кг^-2)
c = 299792458  # Скорость света , м/с
h = 6.62607015e-34  # Постоянная Планка, Дж·с
eV_to_J = 1.602176634e-19  #  эВ в Дж
THz_to_Hz = 1e12  # ТГц в Гц
nm_to_m = 1e-9  # 1 нм в метры


# эВ в Дж
def ev_to_j(energy_eV):
    return energy_eV * eV_to_J

#  Дж в эВ
def j_to_ev(energy_J):
    return energy_J / eV_to_J

# частоты в Гц в ТГц
def hz_to_thz(frequency_hz):
    return frequency_hz / THz_to_Hz

# частоты в ТГц в Гц
def thz_to_hz(frequency_thz):
    return frequency_thz * THz_to_Hz

# энергии в частоту
def energy_to_frequency(energy_J):
    return energy_J / h

# частоты в энергию
def frequency_to_energy(frequency_hz):
    return frequency_hz * h

#  волны в частоту
def wavelength_to_frequency(wavelength_m):
    return c / wavelength_m

# волны в энергию
def wavelength_to_energy(wavelength_m):
    return h * c / wavelength_m

# энергии в длину волны
def energy_to_wavelength(energy_J):
    return h * c / energy_J

energy_eV = 3.26
energy_J = ev_to_j(energy_eV)
frequency_hz = energy_to_frequency(energy_J)
frequency_thz = hz_to_thz(frequency_hz)

test1 = 510
test2 = hz_to_thz(test1)
test3 = frequency_to_energy(test2)
test4 = j_to_ev(test3)

wavelength_nm = 480
wavelength_m = wavelength_nm * nm_to_m
energy_from_wavelength_J = wavelength_to_energy(wavelength_m)
energy_from_wavelength_eV = j_to_ev(energy_from_wavelength_J)


print(f"\nДЛИНА ВОЛНЫ В ЭНЕРГИЮ:\n")
print(f"Длина волны: {wavelength_nm:.2f} нм")
print(f"Энергия: {energy_from_wavelength_eV} эВ")


print(f"\nЧастота В ЕНЕРГИЮ\n")
print(f"Частота:  {test1:.2f} ТГц")
print(f"Энергия: {test4} эВ ")

print(f"\nЕНЕРГИЯ В ЧАСТОТУ\n")
print(f"Энергия: {energy_eV} эВ ")
print(f"Частота:  {frequency_thz} ТГц")

print("_"*100)
M_San = 1.989E30
R_s = (2* M_San * G)/c**2
print(f"\n R_s : {R_s} ")
M_bl_h = h/(R_s*c)
print(f"\n M_bl_h: {M_bl_h} ")