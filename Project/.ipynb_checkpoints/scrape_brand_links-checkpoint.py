{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1cbb34e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f729a47a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get Response of \"brandlist\" Website from Sephora\n",
    "band_lst_link = \"https://www.sephora.com/brands-list\"\n",
    "response = requests.get(band_lst_link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60a714da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use BeautifulSoup\n",
    "soup = BeautifulSoup(response.content, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ec118da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scraping brand links and save them into a list\n",
    "brand_link_lst = []\n",
    "main_box = soup.find_all(attrs={\"data-comp\": \"BrandsList Container Box \"})[0]\n",
    "for brand in main_box.find_all('li'):\n",
    "    brand_link_lst.append(\"https://www.sephora.com\" +\n",
    "                          brand.a.attrs['href']+\"/all?pageSize=300\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da48a50a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write brand links into a file:\n",
    "with open('data/brand_link.txt', 'w') as f:\n",
    "    for item in brand_link_lst:\n",
    "        f.write(f\"{item}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2524120",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Indicate scraping completion\n",
    "print(f'Got All Brand Links! There are {len(brand_link_lst)} brands in total.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "634c4614",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
