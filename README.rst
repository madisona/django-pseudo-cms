
Pseudo CMS
==========

A real basic, fake kind of CMS. Allows you to add just a tiny bit
of dynamic content to your pages.

Overview
********
I often find as a developer I want full control of the page, but there
are small pieces I want a non-technical person to be able to change, or
myself be able to change without additional code / deployment.

This allows you to let a user customize the title tag, meta description,
page title, page body, and a single page image. It will only allow you
to save a ``content`` model to an existing url path that is resolvable
in your django project.

Installation
************

::

  pip install django-pseudo-cms


Usage
*****
add ``pseudo_cms`` to your ``INSTALLED_APPS`` setting.

If you want to change the image and/or thumbnail size of the page's
content image, add the following directives to your settings as they apply. ::

  PSEUDO_CMS_IMAGE_SIZE = (300, 300)
  PSEUDO_CMS_THUMBNAIL_SIZE = (150, 150)

The tuple refers to (width, height). If you'd like to force the image to
a particular size without maintaining its aspect ratio, add a third item
``True`` to your tuple.



