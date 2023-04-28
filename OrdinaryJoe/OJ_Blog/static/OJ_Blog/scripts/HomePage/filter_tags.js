
document.addEventListener('DOMContentLoaded', function() {

    const searchInput = document.getElementById('search-input');
    const allTags = document.querySelectorAll('.tag-filter-all-list .tag-box');
    const appliedTags = document.querySelector('.tag-filter-applied-list');

    // Add event listeners to all tag-box elements in the all tags list
    searchInput.addEventListener('input', (event) => {
        const searchTerm = event.target.value.toLowerCase();

        allTags.forEach((tag) => {
            const tagText = tag.innerText.toLowerCase();

            if (tagText.includes(searchTerm)) {
                tag.style.display = "inline-block";
            } else {
                tag.style.display = "none";
            }
        });
          // Remove all applied tags from the all tags list
        appliedTags.querySelectorAll('.tag-box').forEach((appliedTag) => {
            allTags.forEach((tag) => {
              if (tag.textContent.trim() === appliedTag.textContent.trim()) {
                tag.style.display = 'none';
              }
            });
        });
    });

    // Add event listeners to all tag-box elements in the all tags list
    allTags.forEach(tagBox => {
        tagBox.addEventListener('click', () => {
            // Add the clicked tag to the applied tags list
            const tagText = tagBox.textContent.trim();                  // get the clicked tag's text

            const newTag = document.createElement('div');               // Creating a copy element
            newTag.classList.add('tag-box');
            const tag_text = document.createElement('p');
            tag_text.textContent = tagText;
            newTag.appendChild(tag_text)

            const closeButton = document.createElement('a');
            closeButton.classList.add('close-btn');
            closeButton.innerHTML = '<i class="fas fa-times" style="color:white;"></i>';
            closeButton.style.marginLeft= "auto";
            closeButton.addEventListener('click', () => {
                // Remove the clicked tag from the applied tags list
                newTag.remove();
                // Add the removed tag back to the all tags list
                allTags.forEach(tag => {
                    if (tag.textContent.trim() === tagText) {
                      tag.style.display = 'inline-block';
                    }
                });
                // If there are no applied tags left, show the "None" tag
                if (appliedTags.children.length === 0) {
                    const noneTag = document.createElement('div');
                    noneTag.classList.add('tag-box');
                    noneTag.textContent = 'None';
                    appliedTags.appendChild(noneTag);
                }
            });
            newTag.appendChild(closeButton);

            appliedTags.appendChild(newTag);
            // Hide the clicked tag from the all tags list
            tagBox.style.display = 'none';
            // Remove the "None" tag from the applied tags list
            const noneTag = appliedTags.querySelector('.tag-box');
            if (noneTag.textContent.trim() === "None") {
              noneTag.remove();
            }
            filterPosts();
        });
    });

    // Add event listeners to all tag-box elements in the applied tags list
    appliedTags.addEventListener('click', event => {
        if (event.target.matches('.tag-box')) {
            const tagText = event.target.textContent.trim();
            event.target.remove();
            allTags.forEach(tag => {
            if (tag.textContent.trim() === tagText) {
                tag.style.display = 'inline-block';
            }
        });

        // If there are no applied tags left, show the "None" tag
        if (appliedTags.children.length === 0) {
          const noneTag = document.createElement('div');
          noneTag.classList.add('tag-box');
          noneTag.textContent = 'None';
          appliedTags.appendChild(noneTag);
        }
      }
      filterPosts();
    });
});


function filterPosts() {
    const appliedTags = document.querySelectorAll('.tag-filter-applied-list .tag-box');
    const postContainers = document.querySelectorAll('.post-container');

    postContainers.forEach((postContainer) => {
        // const tags = postContainer.dataset.tags.split(' ');
        const tagsString = postContainer.dataset.tag;
        const tags = tagsString === 'None' ? [] : tagsString.split(' ');
        let showPost = true;
        appliedTags.forEach((tag) => {
            if (tag.textContent.trim() === "None"){
                showPost = true;
            }else if (!tags.includes(tag.textContent.trim())) {
                showPost = false;
            }
        });
        if (showPost) {
            console.log('Showing post container:', postContainer);
            postContainer.classList.remove('hide');
            postContainer.classList.add('show');

        } else {
            console.log('Hiding post container:', postContainer);
            postContainer.classList.add('hide');
            postContainer.classList.remove('show');
        }
    });
}
