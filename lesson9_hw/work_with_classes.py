class Substance:
    STANDARD_TEMPERATURE = 273.15  # температура в K, равная 0 °C
    STANDARD_PRESSURE = 101325  # стандартное давление в Pa
    AVOGADRO_CONSTANT = 6.02214076e23  # постоянная Авогадро

    STATES = ["твердое", "жидкое", "газообразное"]
    PHYSICAL_PROPERTIES = ["плотность",
                           "температура плавления",
                           "температура кипения",
                           "цвет",
                           "агрегатное состояние"
                           ]

    substances_count = 0

    def __init__(self,
                 name,
                 formula,
                 molar_mass,
                 density,
                 state=None,
                 melting_point=None,
                 boiling_point=None
                 ):
        self.name = name
        self.formula = formula
        self.molar_mass = molar_mass
        self.density = density
        self.melting_point = melting_point
        self.boiling_point = boiling_point
        self.state = state
        Substance.substances_count += 1

    @classmethod
    def get_physical_properties(cls):
        """
        Возвращает список физических свойств вещества
        """
        return cls.PHYSICAL_PROPERTIES

    @classmethod
    def get_physical_states(cls):
        """
        Возвращает список агрегатных состояний вещества
        """
        return cls.STATES

    @classmethod
    def get_substances_cont(cls):
        """
        Подсчитывает количество созданных веществ
        """
        return cls.substances_count

    @classmethod
    def get_default_conditions(cls):
        """
        Возвращает стандартные значения температуры и давления
        """
        return (f"Стандартная температура - {cls.STANDARD_TEMPERATURE} K" +
                "\n" +
                f"Cтандартное давление - {cls.STANDARD_PRESSURE} Pa"
                )

    @staticmethod
    def count_atoms_in_amount(quantity):
        """
        Вычисление количества атомов в веществе
        заданного химического количества
        """
        return Substance.AVOGADRO_CONSTANT * quantity

    def calculate_mass(self, quantity):
        """
        Вычисление массы вещества
        """
        mass = self.molar_mass * quantity
        return mass

    def calculate_volume(self, mass):
        """
        Вычисление объема вещества
        """
        volume = mass / self.density
        return volume

    def __str__(self):
        """
        Описание вещества для класса Substance
        """
        return (f"Вещество: {self.name}\n"
                f"Формула: {self.formula}\n"
                f"Молекулярная масса: {self.molar_mass} г/моль\n"
                f"Плотность: {self.density} г/cм³\n"
                f"Агрегатное состояние: {self.state}\n"
                f"Температура плавления: {self.melting_point} °C\n"
                f"Температура кипения: {self.boiling_point} °C\n"
                )


water = Substance(name="вода", formula="H2O", molar_mass=18, density=1)
sodium_hydroxide = Substance(
    name="гидроксид натрия",
    formula="NaOH",
    molar_mass=40,
    density=2.13,
    melting_point=323,
    state="твердое"
)

print(sodium_hydroxide)

chemical_quantity = float(
    input("Введите химическое количество вещества для расчетов: ")
)
water_mass = water.calculate_mass(chemical_quantity)
sodium_hydroxide_mass = sodium_hydroxide.calculate_mass(chemical_quantity)
sodium_hydroxide_volume = round(
    sodium_hydroxide.calculate_volume(sodium_hydroxide_mass), 3
)
atoms_number = Substance.count_atoms_in_amount(chemical_quantity)
print(f"Масса вещества {water.name} составляет {water_mass} г.")
print(f"Объем вещества {sodium_hydroxide.formula}"
      f" составляет {sodium_hydroxide_volume} cm³"
      )
print(f"Количество атомов в {chemical_quantity} моль вещества = {atoms_number}")
print(Substance.get_default_conditions())
print(f"Количество созданных веществ - {Substance.get_substances_cont()}")


class Acid(Substance):
    def __init__(self,
                 name,
                 formula,
                 molar_mass,
                 density,
                 state=None,
                 melting_point=None,
                 boiling_point=None,
                 acid_type=None,
                 water_solubility=None,
                 pKa=None
                 ):
        super().__init__(name,
                         formula,
                         molar_mass,
                         density,
                         state,
                         melting_point,
                         boiling_point
                         )
        self._acid_type = acid_type
        self.water_solubility = water_solubility
        self.pKa = pKa
        self.__melting_point_in_kelvins = self.melting_point + super().STANDARD_TEMPERATURE
        self.__boiling_point_in_kelvins = self.boiling_point + super().STANDARD_TEMPERATURE

    def get_temperatures_in_kelvins(self):
        """
        Через функцию возвращаем приватные значения
        температуры плавления и кипения в Кельвинах
        """
        return self.__melting_point_in_kelvins, self.__boiling_point_in_kelvins

    def __str__(self):
        """
        Переопределенный метод описания вещества
        для класса Acid
        """
        description = super().__str__()
        description += (f"Тип кислоты: {self._acid_type}\n"
                        f"Растворимость в воде: {self.water_solubility}\n"
                        f"Константа диссоциации pKa: {self.pKa}\n"
                        )
        return description


sulfuric_acid = Acid(
    name="серная кислота",
    formula="H2SO4",
    molar_mass=98,
    density=1.8356,
    state="жидкое",
    boiling_point=337,
    melting_point=10.38,
    acid_type="неорганическая",
    water_solubility="хорошо растворяется в воде",
    pKa=-3
)
print(sulfuric_acid)
temperatues_in_kelvins = sulfuric_acid.get_temperatures_in_kelvins()
print(f"Температура плавления: {temperatues_in_kelvins[0]} K",
      f"Температура кипения: {temperatues_in_kelvins[1]} K", sep="\n")
sulfuric_acid_mass = sulfuric_acid.calculate_mass(chemical_quantity)
print(f"Масса вещества {sulfuric_acid.formula} составляет {sulfuric_acid_mass} г.")
print(f"Физические свойства вещества:\n{Acid.get_physical_properties()}")
