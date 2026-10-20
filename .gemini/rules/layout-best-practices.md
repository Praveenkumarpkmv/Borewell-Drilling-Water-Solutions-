---
description: "Core CSS layout and Tailwind best practices for alignment and responsiveness."
---
# CSS & Layout Rules

When writing or modifying HTML/Tailwind CSS in this project, you MUST adhere to the following structural principles to prevent broken layouts:

### 1. Vertical Alignment in Card Grids (Crucial)
When creating a row of cards where each card has a Title and a Description, you must ensure the descriptions start at the exact same vertical baseline across all cards.
*   **Rule:** Apply a fixed `min-h-[X]` (e.g., `min-h-[3.5rem]` for 2 lines of text) to the Title (`<h3>` or `<h4>`) elements. This guarantees that whether a title fits on 1 line or wraps to 2 lines, it reserves the same vertical space, keeping the content below it perfectly aligned.

### 2. Equal Height Flex Cards & Buttons
*   **Rule:** Use `items-stretch` on grid containers so all cards stretch to the height of the tallest card in the row.
*   **Rule:** Inside the card, use `flex flex-col h-full`. Apply `flex-grow` (or `mb-auto`) to the middle content (like descriptions or lists) so that the call-to-action buttons at the bottom of the cards are pushed down and aligned perfectly horizontally across the row.

### 3. Preventing Awkward Text Wrapping
*   **Rule:** Use `whitespace-nowrap` on any text that should NEVER break across multiple lines. 
*   This specifically applies to: 
    - Pricing formats (e.g., `$199 / unit`)
    - Numbers with units or metrics (e.g., `620 ft`, `12K L`)
    - Navigation bar links (`.nav-link`)

### 4. Flexbox Distortion Prevention
*   **Rule:** Always apply `shrink-0` to fixed-size elements (like circular avatars, icon badges, or logo containers) when they are inside a `flex` container. This prevents flexbox from squishing them into ovals when the adjacent text content requires more space.

### 5. Grid Column Constraints & Truncation
*   **Rule:** Do not force too many columns (e.g., `grid-cols-4`) into small container widths. If the text requires `white-space: nowrap`, forcing it into narrow columns will cause overflow or truncation.
*   **Solution:** Default to `grid-cols-2` for metric grids or stat chips to give the text enough 50% width breathing room to stay fully visible without getting chopped off by `overflow: hidden`.

### 6. Responsive Design Across All Devices
*   **Rule:** Every layout must be fully responsive and tested logically across all dimensions, from small mobile screens to large desktop monitors.
*   **Implementation:** 
    - Utilize Tailwind's responsive breakpoints (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`) to adjust grid columns, padding, font sizes, and layout flow progressively.
    - Default to single-column stacking (`grid-cols-1` or `flex-col`) on base mobile views to prevent horizontal scrolling or cramped content.
    - Expand to multi-column layouts only on larger breakpoints (`sm:grid-cols-2`, `lg:grid-cols-3`, etc.) when there is mathematically enough physical screen space for the content to breathe.
