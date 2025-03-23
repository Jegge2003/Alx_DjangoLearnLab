# Django Blog Project

## CRUD Functionality

### Features:
- View all posts (`/posts/`)
- View post details (`/posts/<id>/`)
- Create post (`/posts/new/`) [Login required]
- Edit post (`/posts/<id>/edit/`) [Author only]
- Delete post (`/posts/<id>/delete/`) [Author only]

### User Permissions:
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.

### How to Test:
1. Register/Login at `/register` and `/login`.
2. Create a new post.
3. View and edit/delete your posts.
4. Ensure you can't edit/delete others' posts.

---

## ✅ Deliverables Recap

- **Python Files**  
  - `views.py`: All CRUD views  
  - `urls.py`: URL patterns  
  - `forms.py`: Optional ModelForm  
  - `models.py`: `Post` model already done  

- **Templates**  
  - `post_list.html`  
  - `post_detail.html`  
  - `post_form.html`  
  - `post_confirm_delete.html`  

- **Documentation**  
  - `README.md`

---

Let me know if you need:
✔ Pagination on ListView  
✔ Search bar  
✔ Categories/tags for posts  
✔ Profile pictures / Author bios  
I'm here to help you polish it!
