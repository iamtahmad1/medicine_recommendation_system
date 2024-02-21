import scrapy

class MateriamedicaSpider(scrapy.Spider):
    name = 'materiamedica'
    allowed_domains = ['materiamedica.info']
    start_urls = ['https://www.materiamedica.info/en/materia-medica/william-boericke/']

    def parse(self, response):
        # Extract all <h1> tags
        h1_tags = response.css('h1::text').getall()
        p_tags = response.css('p::text').getall()
        medicine_data = {}

        # Extract <h1> tags with capital letters and put them under the "medicine name" column
        medicine_names = []
        for h1_tag in h1_tags:
            if h1_tag.strip().isupper():  # Check if all characters in the tag are capitalized
                medicine_names.append(h1_tag.strip())
        
        if medicine_names:
            medicine_data['medicine_name'] = medicine_names

        # Iterate over each <p> tag
        for p_tag in p_tags:
            # Check if the text contains ".--"
            if ".--" in p_tag:
                # Split the text by ".--"
                parts = p_tag.split(".--", 1)
                if len(parts) == 2:
                    column_name, medicine = parts
                    # Remove leading and trailing whitespace
                    column_name = column_name.strip()
                    medicine = medicine.strip()
                    # Add the medicine information to the dictionary
                    if column_name not in medicine_data:
                        medicine_data[column_name] = [medicine]
                    else:
                        medicine_data[column_name].append(medicine)

        yield medicine_data

        # Follow links to other pages under the specified URL
        for next_page in response.css('a::attr(href)').getall():
            if next_page.startswith('/en/materia-medica/william-boericke/'):
                yield response.follow(next_page, self.parse)
